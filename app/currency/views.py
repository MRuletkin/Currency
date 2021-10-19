from currency.models import Rate, ContactUs

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
    obj = ContactUs.objects.all()

    for _ in obj:
        results.append(
            f'ID: {_.id}, sale: {_.email_from}, buy: {_.subject}, created: {_.message}<br>')

    return HttpResponse(str(results))
