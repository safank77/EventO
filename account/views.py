from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView,CreateView,DetailView,View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
# Create your views here.

class HomeView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("Username")
            pswd=form_data.cleaned_data.get("Password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"login successfull")
                return redirect('evt')
            else:
                messages.error(request,"sign in failed !! Please check you username and password")
                
                return redirect("h")
        return render(request,"login.html",{"form":form_data})
    

class Logout(View):
    def get(self,request):
        
        logout(request)
        return redirect('h')    



class RegView(CreateView):

    template_name="reg.html"
    model=User
    form_class=RegForm
    success_url=reverse_lazy("h")
    
    def form_valid(self,form):
        messages.success(self.request,"Registeration successfull")
        return super().form_valid(form)