from django.shortcuts import render

from currency.models import ContactUs, Rate

from django.http.response import HttpResponse


def rate_list(request):

    rates = Rate.objects.all()
    context = {
        'rates': rates,
    }
    return render(request, 'rate_list.html', context)


def contact_us(request):
    results = []
    objects = ContactUs.objects.all()

    for object_ in objects:
        results.append(
            f'ID: {object_.id}, email_from: {object_.email_from}, subject: {object_.subject}, message: {object_.message}<br>')

    return HttpResponse(str(results))


