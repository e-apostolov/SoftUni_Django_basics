from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from urlsAndViews.department.models import Department

def index(request):
    url = reverse('redirect-view')
    url_lazy = reverse_lazy('redirect-view')
    return HttpResponse(f"<h1>{url_lazy}</h1>")

def view_with_name(request, variable):
    return render(request,'departments/name_template.html',{"variable": variable})

def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args} Kwargs: {kwargs}</h1>")

def view_with_int_pk(request, pk: int):
    return HttpResponse(f"<h1>Int pk with pk: {pk}</h1>")

def view_with_slug(request, pk, slug):
    department = Department.objects.filter(pk=pk, slug=slug)

    if not department:
        raise Http404
    return HttpResponse(f"<h1>Department from slug: {department}</h1>")

def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")

def redirect_to_softuni(request):
    return redirect('https://www.softuni.bg/')

def redirect_to_view(request):
    return redirect('numbers', pk=2)