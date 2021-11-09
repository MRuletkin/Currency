from currency.forms import RateForm, SourceForm
from currency.models import ContactUs, Rate, Source

from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)


class RateListView(ListView):
    queryset = Rate.objects.all()


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'currency/rate_create.html'


class RateUpdateView(UpdateView):
    form_class = RateForm
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'currency/rate_update.html'


class RateDetailsView(DetailView):
    model = Rate


class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('currency:rate-list')


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

    def _send_email(self):
        subject = 'User'
        body = f'''
            Request From: {self.object.name}
            Email to reply: {self.object.reply_to}
            Body: {self.object.body}
            Subject: {self.object.subject}
        '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect


class SourceListView(ListView):
    queryset = Source.objects.all()


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'currency/source_create.html'


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'currency/source_update.html'


class SourceDetailsView(DetailView):
    model = Source


class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'currency/source_delete.html'
    success_url = reverse_lazy('currency:source-list')


# def contact_us(request):
#
#     objects = ContactUs.objects.all()
#     context = {
#         'contact_us': objects,
#     }
#     return render(request, 'contactus_list.html', context)
#
#
# def source_list(request):
#
#     objects = Source.objects.all()
#     context = {
#         'source_list': objects,
#     }
#     return render(request, 'source_list.html', context)
#
#
# def source_create(request):
#     if request.method == 'POST':
#         form = SourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/list')
#     else:
#         form = SourceForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'source_create.html', context)
#
#
# def source_update(request, pk):
#
#     instance = get_object_or_404(Source, id=pk)
#
#     if request.method == 'POST':
#         form = SourceForm(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/list')
#     else:
#         form = SourceForm(instance=instance)
#
#     context = {
#         'form': form
#     }
#     return render(request, 'source_update.html', context)
#
#
# def source_delete(request, pk):
#
#     instance = get_object_or_404(Source, id=pk)
#
#     if request.method == 'GET':
#         context = {
#             'source_list': instance,
#         }
#         return render(request, 'source_delete.html', context)
#     else:
#         instance.delete()
#         return HttpResponseRedirect('/source/list')
#
#
# def source_details(request, pk):
#
#     instance = get_object_or_404(Source, id=pk)
#
#     context = {
#         'object': instance,
#     }
#     return render(request, 'source_detail.html', context)
