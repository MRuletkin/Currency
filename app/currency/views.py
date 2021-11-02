from django.http import HttpResponseRedirect, Http404

from currency.models import ContactUs, Rate, Source

from django.shortcuts import render, get_object_or_404

from currency.forms import RateForm, SourceForm


def rate_list(request):

    rates = Rate.objects.all()
    context = {
        'rates': rates,
    }
    return render(request, 'rate_list.html', context)


def rate_create(request):
    if request.GET:
        form = RateForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list')
    else:
        form = RateForm()

    context = {
        'form': form
    }
    return render(request, 'rate_create.html', context)


def contact_us(request):

    objects = ContactUs.objects.all()
    context = {
        'contact_us': objects,
    }
    return render(request, 'contact_us.html', context)


def source_list(request):

    objects = Source.objects.all()
    context = {
        'source_list': objects,
    }
    return render(request, 'source_list.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list')
    else:
        form = SourceForm()

    context = {
        'form': form
    }
    return render(request, 'source_create.html', context)


def source_update(request, pk):

    instance = get_object_or_404(Source, id=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list')
    else:
        form = SourceForm(instance=instance)

    context = {
        'form': form
    }
    return render(request, 'source_update.html', context)


def source_delete(request, pk):

    instance = get_object_or_404(Source, id=pk)

    if request.method == 'GET':
        context = {
            'source_list': instance,
        }
        return render(request, 'source_delete.html', context)
    else:
        instance.delete()
        return HttpResponseRedirect('/source/list')


def source_details(request, pk):

    instance = get_object_or_404(Source, id=pk)

    context = {
        'object': instance,
    }
    return render(request, 'source_details.html', context)
