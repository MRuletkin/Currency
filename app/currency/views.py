from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source
from currency.tasks import send_email_in_background

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)


class RateListView(ListView):
    queryset = Rate.objects.all().order_by('-created').select_related('source')


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'currency/rate_create.html'


class RateUpdateView(UserPassesTestMixin, UpdateView):
    form_class = RateForm
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'currency/rate_update.html'

    def test_func(self):
        return self.request.user.is_superuser


class RateDetailsView(LoginRequiredMixin, DetailView):
    model = Rate


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class ContactusListView(ListView):
    queryset = ContactUs.objects.all()


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'currency/contactus_create.html'
    success_url = reverse_lazy('index')
    fields = (
        'name',
        'reply_to',
        'subject',
        'body',
    )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        subject = 'User ContactUs'
        body = f'''
            Request From: {self.object.name}
            Email to reply: {self.object.reply_to}
            Subject: {self.object.subject}
            Body: {self.object.body}
        '''
        send_email_in_background.delay(subject, body)
        # send_email_in_background.apply_async(args=(subject, body))
        '''
        00-8.59 | 9.00-19.00 | 19.01 - 23.59
        9.00    |    send    | 9.00 next day
        '''
        # from datetime import datetime, timedelta
        # eta = datetime(2021, 11, 21, 19, 00, 00)
        # send_email_in_background.apply_async(
        #     kwargs={'subject': subject, 'body': body},
        #     countdown=120,
        # eta=eta,
        # )
        return redirect


class SourceListView(ListView):
    queryset = Source.objects.all().order_by('-created')


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'currency/source_create.html'


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'currency/source_update.html'


class SourceDetailsView(UpdateView):
    model = Source
    template_name = 'currency/source_detail.html'
    success_url = reverse_lazy('currency:source-list')
    fields = (
        'avatar',
    )


class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'currency/source_delete.html'
    success_url = reverse_lazy('currency:source-list')
