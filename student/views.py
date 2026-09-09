from django.shortcuts import render,redirect
from user.models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    data=""
    bid=request.session.get("bid")
    if bid is not None:
        data=tbl_live.objects.all().filter(batch=bid).order_by("-id")[0:1]   
    return render(request,"student/index.html",{"lives":data})

def courses(request):
    cdata=""
    bid=request.session.get("bid")
    if bid is not None:
        cdata=tbl_category.objects.all().filter(batch=bid)
    return render(request,"student/courses.html",{"courses":cdata})

def lectures(request):
    data=""
    bid=request.session.get("bid")
    if bid is not None:
        data=tbl_lectures.objects.all().filter(category__batch=bid)
    return render(request,"student/lectures.html",{"videos":data})

def task(request):
    data=""
    bid=request.session.get("bid")
    if bid is not None:
        data=tbl_task.objects.all().filter(batch=bid)
    return render(request,"student/task.html",{"tasks":data})

def enotes(request):
    data=""
    bid=request.session.get("bid")
    if bid is not None:
        data=tbl_notes.objects.all().filter(batch=bid)
    return render(request,"student/enotes.html",{"notes":data})

def softwarekit(request):
    data=tbl_software.objects.all().order_by("-id")
    return render(request,"student/softwarekit.html",{"softwares":data})

def profile(request):
    data=""
    user=request.session.get("email")
    if user:
        data=tbl_register.objects.all().filter(email=user)
        if request.method=="POST":
            name=request.POST.get("name")
            mobile=request.POST.get("mobile")
            password=request.POST.get("password")
            picture=request.FILES["fu"]
            address=request.POST.get("address")
            tbl_register(name=name,mobile=mobile,password=password,profile_picture=picture,address=address,email=user).save()
            return HttpResponse("<script>alert('Your Profile is Updated Successfully..');location.href='/student/profile/'</script>")
    return render(request,"student/profile.html",{"userinfo":data})

def logout(request):
    user=request.session.get("email")
    if user:
        request.session.flush()
        return redirect("/user/login/")
    return render(request,"student/logout.html")

def liveclass(request):
    data=""
    bid=request.session.get("bid")
    if bid is not None:
        data=tbl_live.objects.all().filter(batch=bid)
    return render(request,"student/liveclass.html",{"lives":data})

def ldetails(request):
    cpic=request.GET.get("pic")
    cid=request.GET.get("cid")
    data=tbl_lectures.objects.all().filter(category=cid)
    return render(request,"student/ldetails.html",{"videos":data,"cpic":cpic})