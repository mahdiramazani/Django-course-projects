from django.shortcuts import render,HttpResponse
from .models import ProfileUSer

def ProfileView(request):


    users=ProfileUSer.objects.all()


    return render(request,"Profile_app/index.html",context={"users":users})


def Profile_User(request,name):

    return render(request,"Profile_app/users.html",context={"name":name})





