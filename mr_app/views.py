from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import InputForm

def index(request):
    if request.method == 'NEXT':
        return HttpResponseRedirect('input/')
    return render(request, 'index.html')

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

