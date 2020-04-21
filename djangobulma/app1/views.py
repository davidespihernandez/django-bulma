from django.shortcuts import render

from app1.forms import ExampleForm


def test(request):
    return render(request, 'app1/test.html', {"var": "value"})


def form(request):
    example_form = ExampleForm()
    return render(request, 'app1/form.html', {"form": example_form, "next": "/path/to/next?"})
