from django.shortcuts import render,redirect
from account.models import *
from django.contrib.auth.models import User
from django .views.generic import TemplateView,ListView,DetailView
from django .contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# Create your views here.

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"please Login first!!")
            return redirect("h")
    return inner  
desc=[never_cache,signin_required] 



@method_decorator(desc,name='dispatch')

class EventMainView(TemplateView):
    template_name="eventmain.html"

@method_decorator(desc,name='dispatch')

class EventSelect(ListView):
    template_name="selectevt.html"
    queryset=Event.objects.all()
    context_object_name="events"

@method_decorator(desc,name='dispatch')

class EventDetails(DetailView):
    template_name="eventdt.html"
    pk_url_kwarg="id"
    queryset=Event.objects.all()
    context_object_name="details"

@method_decorator(desc,name='dispatch')

class EventBook(TemplateView):
    template_name="bookevt.html"    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        event=Event.objects.get(id=id)
        user=request.user
        phone=request.POST.get("phn")
        address=request.POST.get("add")
        date=request.POST.get("dt")
        time=request.POST.get("tm")
        description=request.POST.get("des")


        Book.objects.create(event=event,user=user,phone=phone,address=address,date=date,time=time,description=description)
        event.save()
    
        messages.success(request,"Booking Successful !! ")
        return redirect("bk")
    
    
    
@method_decorator(desc,name='dispatch')

class MyBooking(ListView):
    template_name="mybook.html"
    queryset=Book.objects.all()
    context_object_name="book" 

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

desc
def cancelbooking(request,*args,**kwargs):
    oid=kwargs.get("id")
    book=Book.objects.get(id=oid)
    book.status='Cancelled'
    book.save()
    messages.success(request,"Booking cancelled")    
    return redirect('bk')       