from django import forms

from currency.models import Rate, Source


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = {
            'buy',
            'sale',
            'type',
            'source',
        }


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = {
            'source_url',
            'name',
        }
