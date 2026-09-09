from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    data=tbl_upcomingbatch.objects.all().order_by("-id")[0:2]
    return render(request,"user/index.html",{"data":data})

def contact(request):
    mydict={}
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("mobile")
        c=request.POST.get("email")
        d=request.POST.get("message")
        tblcontact(name=a,mobile=b,email=c,message=d).save()
        mydict={
            "msg":"Thank you for contact with us"
        }
    return render(request,"user/contact.html",mydict)

def gallery(request):
    data=tblgallery.objects.all()
    mydict={'gdata':data}
    return render(request,"user/gallery.html",mydict)

def about(request):
    return render(request,"user/about.html")

def team(request):
    data=tblteam.objects.all()
    mydict={'tdata':data}
    return render(request,"user/team.html",mydict)

def profile(request):
    return render(request,"user/profile.html")

def uprofile(request):
    return render(request,"uprofile.html")

def registration(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Mobile=request.POST.get("mobile")
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        Address=request.POST.get("address")
        ppic=request.FILES["fu"]
        x=tbl_register.objects.all().filter(email=Email).count()
        if x==0:
            tbl_register(name=Name,mobile=Mobile,email=Email,password=Password,address=Address,profile_picture=ppic).save()
            return HttpResponse("<script>alert('You are Registered Successfully...');location.href='/user/registration/'</script>")
        else:
            return HttpResponse("<script>alert('You are Already Registered...');location.href='/user/registration/'</script>")
    return render(request,"user/register.html")

def login(request):
    if request.method=="POST":
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        x=tbl_register.objects.all().filter(email=Email,password=Password).first()
        if x:
            request.session["email"]=str(x.email)
            request.session["uname"]=str(x.name)
            request.session["upic"]=str(x.profile_picture)
            request.session["bid"]=str(x.user_batch.id)
            return HttpResponse("<script>alert('You are Login Successfully...');location.href='/student/index/'</script>")
        else:
            return render(request,"user/login.html",{"msg":"Your Email id or Password is Incorrect..."})
    return render(request,"user/login.html")

def dashboard(request):
    return render(request,"dashboard.html")

def upcomingbatch(request):
    data=tbl_upcomingbatch.objects.all().order_by("-id")
    return render(request,"user/upcomingbatch.html",{"data":data})