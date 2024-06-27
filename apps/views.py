from django.shortcuts import render
from . forms import UserForm
from django.contrib import messages

# Create your views here.

def reg(request):
    if request.method == 'POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'your are data created')
            messages.info(request,'this is success message ')

    else:
        fm=UserForm()
    return render(request,'regestion.html',{'form':fm})