from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, RedirectView

from .forms import StudentRegistration
from .models import User


# This Class will add new data
class AddDisplay(TemplateView):
    template_name = 'enroll/add_display.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'stu': stud, 'form': fm}
        return context

    def post(self, request):
        SR = StudentRegistration(request.POST)

        if SR.is_valid():
            nm = SR.cleaned_data['name']
            em = SR.cleaned_data['email']
            pwd = SR.cleaned_data['password']
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            return HttpResponseRedirect('/')


# This Class will delete the data

class DeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


# This Class will update or edit the data
class UpdateView(View):

    def get(self,request,id):
        pi = User.objects.get(pk=id)
        SR = StudentRegistration(instance=pi)
        return render(request, 'enroll/update.html', {'form': SR})

    def post(self,request,id):
        pi = User.objects.get(pk=id)
        SR = StudentRegistration(request.POST, instance=pi)
        if SR.is_valid():
            SR.save()
        return render(request, 'enroll/update.html', {'form': SR})








