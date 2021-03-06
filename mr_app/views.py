from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms.formsets import formset_factory
from .models import MRInput
from .forms import InputForm
from .worker import Mars, Rover, directions
import sqlite3

#with sqlite3.connect('db.sqlite3') as conn:
conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
c = conn.cursor()

# Redirect URL localhost:8000 to /index/
def redirect_index(request):
    return HttpResponseRedirect('index/')

# Welcome page with instructions and two redirects
def index(request):
    if(request.GET.get('next-btn')):
        return HttpResponseRedirect('input/')
    elif(request.GET.get('delete-btn')):
        return HttpResponseRedirect('del_view/')
    return render(request, 'index.html')

# Input form view, based from MRInput model. SQL ensures uppercase is saved to db for all strings
def input(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            c.execute('UPDATE mr_app_mrinput SET r1pface = upper(r1pface), inst1 = upper(inst1), r2pface = upper(r2pface), inst2 = upper(inst2)')
            conn.commit()
            return HttpResponseRedirect('/index/success/')
    form = InputForm()
    return render(request, 'form.html', {'form': form})

# Success view, to visualy allow user to validate input data, includes two redirects
def success(request):
    user_inputs = MRInput.objects.all().first()
    args = {'user_inputs': user_inputs}
    if(request.GET.get('next-calc-btn')):
        # Should call function to start calculation !!!!!!!!!!!!!!!!!!!!!!!!!
        return redirect('/index/current_position/proceed')
    elif(request.GET.get('back-succ-btn')):
        c.execute('DELETE FROM mr_app_mrinput')
        conn.commit()
        return HttpResponseRedirect('/index/input')
    return render(request, 'success.html', args)

# View to allow user to delete previous data input
def del_view(request):
    if(request.GET.get('sure-delete')):
        c.execute('DELETE FROM mr_app_mrinput')
        conn.commit()
        return HttpResponseRedirect('/index/')
    return render(request, 'del_view.html')

# Worker view, calculations are processed here
def current_position(request, do_calc):
    #if(do_calc == 'proceed'):
    #    return HttpResponse('Test if statement: ' + str(do_calc))
    user_inputs = MRInput.objects.all().first()
    args = {'user_inputs': user_inputs}
    if(do_calc == 'proceed'): # will loop until Mars has been initialized.
        sopx1 = args.sopx
        sopy1 = args.sopy
        if len(sopx1, sopy1): # Checks so that the input is length 2 and then checks type-integrity
            mars = Mars(int(sopx1), int(sopy1))
        else:
            print("Incorrect input. Please ensure you enter a string with two numerical elements")

def rover_do():
    rover = add_rover(mars)# Initiate a rover with the supplied input. Each rover is assigned to a Mars (many-to-one relation).
    move_rover(rover, mars)

    # Must add and complete methods for adding rover and then moving rover.
    #rover = add_rover(mars)       # Initiate a rover with the supplied input. Each rover is assigned to a Mars (many-to-one relation).
    #move_rover(rover, mars)