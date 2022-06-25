from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from ad.forms import AdForm
from ad.models import Ad


class AdIndexView(ListView):
    model = Ad
    context_object_name = "ads"
    template_name = "ads/index.html"
    ordering = ["-publication_date"]


class AdCreateView(CreateView):
    model = Ad
    template_name = "ads/create.html"
    form_class = AdForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdDetailView(DetailView):
    template_name = "ads/detail.html"
    model = Ad
    context_object_name = 'ads'


class AdDeleteView(DeleteView):
    model = Ad
    template_name = 'ads/delete.html'
    success_url = reverse_lazy('ads:index')


class AdUpdateView(UpdateView):
    form_class = AdForm
    template_name = "ads/update.html"
    model = Ad
