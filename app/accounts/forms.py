import uuid

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse_lazy


class UserSignUpForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = {
            'email',
        }

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password_confirm']:
                raise forms.ValidationError("Passwords don't match.")
            return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.username = str(uuid.uuid4())
        user.save()  # <- save user to database
        self._send_email()
        return user

    def _send_email(self):
        subject = 'Thanks for sign up'
        path = reverse_lazy('accounts:activate', args=(self.instance.username,))
        body = f'''
        {settings.HTTP_SCHEMA}://{settings.DOMAIN}{path}
        '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [self.instance.email],
            fail_silently=False,
        )
