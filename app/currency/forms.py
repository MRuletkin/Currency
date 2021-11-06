from currency.models import ContactUs, Rate, Source

from django import forms


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = {
            'buy',
            'sale',
            'type',
            'source',
        }


class ContactusForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = {
            'email_from',
            'subject',
            'message',
        }


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = {
            'source_url',
            'name',
        }
