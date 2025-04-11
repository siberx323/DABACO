from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
   # return HttpResponse("welcome")
   hom=homepage.objects.all()
   return render(request,"mainapp/index.html",context={"hom":hom})
def about(request):
   # return HttpResponse("welcome")
   st=staticcontentclass.objects.get(key='about')
   return render(request,"mainapp/about.html",context={"matn": st})
def services(request):
   # return HttpResponse("welcome")
   cat=categoryclass.objects.all()
   return render(request,"mainapp/services.html",context={"cat":cat})
def contact(request):
   # return HttpResponse("welcome")
   if (request.method=="POST"):
      f=contactform(request.POST)
      if (f.is_valid):
          f.save()
          messages.success(request, 'پیام شما با موفقیت ارسال شد.')  # پیام موفقیت
          return redirect("/contact")
   else:
    f=contactform()
    st=staticcontentclass.objects.get(key='contact')
    return render(request,"mainapp/contact.html",context={"f":f,"matn": st})
def showservice(request,adad):
    ser=servicesclass.objects.filter(category_id=adad)
    return render(request,"mainapp/showservice.html",context={"ser":ser})