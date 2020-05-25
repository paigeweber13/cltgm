from django.shortcuts import render
from cltgm import constants

def home(request):
    context = {
        'constants': constants,
    }
    return render(request, 'cltgm/index.html', context)

def what_is_dnd(request):
    context = {
    }
    return render(request, 'cltgm/info/what-is-dnd.html', context)

def pricing(request):
    context = {
    }
    return render(request, 'cltgm/info/pricing.html', context)

def for_parents(request):
    context = {
    }
    return render(request, 'cltgm/info/for-parents.html', context)

def contact_me(request):
    context = {
    }
    return render(request, 'cltgm/info/contact-me.html', context)
