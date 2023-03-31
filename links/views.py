# SHORTLY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

import re
from .models import Link
from .forms import LinkForm
from django.shortcuts import redirect
from django.shortcuts import render

def add_link(request):
    """
    We accept user input
    and save it to the database.
    """
    if request.method == 'POST':
        url_regex = r'http|https\:\/\/[a-z0-9]\/+'
        form = LinkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            if re.match(url_regex, url):
                name = form.cleaned_data.get('name')
                date = form.cleaned_data.get('date')
                link_entry = Link(name=name, url=url, date=date)
                link_entry.save()
                return redirect('links:link', pk=link_entry.pk)
            else:
                regex_error = 'No valid URL string supplied.'
                return redirect('links:error', err=regex_error)
        else:
            error_msg = 'Form could not be processed.'
            return redirect('links:error', err=error_msg)
    else:
        form = LinkForm()
    return render(request, 'links/home.html', {'form': form})

def link(request, pk):
    """
    You can view
    information about
    a submitted link here.
    """
    item = Link.objects.get(pk=pk)
    name = item.name
    url = item.url
    date = item.date
    pk = pk
    root_url = request.get_host()
    context = {
        'name': name,
        'url': url,
        'date': date,
        'pk': pk,
        'root_url':root_url
    }
    return render(request, 'links/item.html', context)

def error(request, err):
    """
    An error view when stuff goes wrong.
    """
    return render(request, 'links/error.html', {'error':err})

def redirect_to(request, pk):
    """
    The finished shortened URL view.
    """
    item = Link.objects.get(pk=pk)
    url = item.url
    return redirect(url)