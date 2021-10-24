from currency.models import ContactUs, Rate

from django.shortcuts import render


def rate_list(request):

    rates = Rate.objects.all()
    context = {
        'rates': rates,
    }
    return render(request, 'rate_list.html', context)


def contact_us(request):

    objects = ContactUs.objects.all()
    context = {
        'contact_us': objects,
    }
    return render(request, 'contact_us.html', context)
