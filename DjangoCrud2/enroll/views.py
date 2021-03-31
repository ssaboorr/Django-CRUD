from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# This Function will add new data
def add_display(request):
    if request.method == 'POST':
        SR = StudentRegistration(request.POST)
        if SR.is_valid():
            nm = SR.cleaned_data['name']
            em = SR.cleaned_data['email']
            pwd = SR.cleaned_data['password']
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            SR = StudentRegistration()

            # SR.save()
    else:
        SR = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/add_display.html', {'form': SR, 'stu': stud})


# This Function will delete the data
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# This function will update or edit the data
def update_edit(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        SR = StudentRegistration(request.POST, instance=pi)
        if SR.is_valid():
            SR.save()
    else:
        pi = User.objects.get(pk=id)
        SR = StudentRegistration(instance=pi)
    return render(request, 'enroll/update.html', {'form': SR})





