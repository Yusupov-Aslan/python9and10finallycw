from django import forms

from ad.models import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('photo', 'title', 'text', 'coast', 'category', )


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")
