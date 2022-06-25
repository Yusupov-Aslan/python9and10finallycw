from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from ad.forms import AdForm, SearchForm
from ad.models import Ad


class SearchView(ListView):
    search_form_class = SearchForm
    search_form_field = "search"
    search_fields = []

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = self.get_query()
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form_class()
        if self.search_value:
            context['form'] = self.search_form_class(initial={self.search_form_field: self.search_value})
            context[self.search_form_field] = self.search_value
        return context

    def get_form(self):
        return self.search_form_class(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get(self.search_form_field)

    def get_query(self):
        query = Q()
        for field in self.search_fields:
            kwargs = {field: self.search_value}
            query = query | Q(**kwargs)
        return query


class AdIndexView(SearchView):
    model = Ad
    context_object_name = "ads"
    template_name = "ads/index.html"
    paginate_by = 3
    paginate_orphans = 0
    ordering = ["-publication_date"]
    search_fields = ["title__icontains", "author__username__icontains"]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status="published")
        if self.search_value:
            query = self.get_query()
            queryset = queryset.filter(query)
        return queryset


class AdCreateView(PermissionRequiredMixin, CreateView):
    model = Ad
    template_name = "ads/create.html"
    form_class = AdForm
    permission_required = "ad.add_ad"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdDetailView(DetailView):
    template_name = "ads/detail.html"
    model = Ad
    context_object_name = 'ads'


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    model = Ad
    template_name = 'ads/delete.html'
    success_url = reverse_lazy('ads:index')
    permission_required = "ad.delete_ad"

class AdUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = AdForm
    template_name = "ads/update.html"
    model = Ad
    permission_required = "ad.change_ad"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author


class AdModerateView(LoginRequiredMixin, SearchView):
    model = Ad
    template_name = "ads/moderated.html"
    paginate_by = 3
    paginate_orphans = 0
    context_object_name = "ads"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status="moderated")
        if self.search_value:
            query = self.get_query()
            queryset = queryset.filter(query)
        return queryset
