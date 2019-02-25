from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import MRInput
from .forms import InputForm
import sqlite3

#with sqlite3.connect('db.sqlite3') as conn:
conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
c = conn.cursor()

def redirect_index(request):
    return HttpResponseRedirect('index/')

def index(request):
    if(request.GET.get('next-btn')):
        return HttpResponseRedirect('input/')
    elif(request.GET.get('delete-btn')):
        return HttpResponseRedirect('del_view/')
    return render(request, 'index.html')

def input(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
            return HttpResponseRedirect('/index/success/')
    form = InputForm()
    return render(request, 'form.html', {'form': form})

def success(request):
    return HttpResponse("success placeholder")

def del_view(request):
    if(request.GET.get('sure-delete')):
        #c.execute('SELECT * FROM mr_app_mrinput')
        c.execute('DELETE FROM mr_app_mrinput')
        conn.commit()
        #data = c.fetchall()
        return HttpResponseRedirect('/index/')
        #return HttpResponse(str(data))
    return render(request, 'del_view.html')

