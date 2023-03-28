from django.shortcuts import render,HttpResponse
from .models import Profile

def ProfileView(request):

    users=Profile.objects.all()
    
    return render(request,"Profile_app/index.html",context={"users":users})


def ProfileUser(request,name):


    return render(request,"Profile_app/user.html",context={"name":name})



