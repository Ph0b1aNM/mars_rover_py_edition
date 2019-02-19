from django.http import HttpResponse
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

    form = InputForm()
    return render(request, 'form.html', {'form': form})