from currency.models import ContactUs, Rate

from django.http.response import HttpResponse


def rate_list(request):

    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, sale: {rate.sale}, buy: {rate.buy}, created: {rate.created}, source: {rate.source}<br>')

    return HttpResponse(str(results))


def contact_us(request):
    results = []
    objects = ContactUs.objects.all()

    for object_ in objects:
        results.append(
            f'ID: {object_.id}, email_from: {object_.email_from}, subject: {object_.subject}, message: {object_.message}<br>')

    return HttpResponse(str(results))
