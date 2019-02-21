from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import InputForm

def index(request):
    return HttpResponse("Hello, world. You're at the mr_app index.")

def input(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
            return HttpResponseRedirect('success/')
    form = InputForm()
    return render(request, 'form.html', {'form': form})

def success(request):
    return HttpResponse("placeholder")

