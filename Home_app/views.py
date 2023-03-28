from django.shortcuts import render,HttpResponse

def HomeView(request):


    return render(request,"Home_app/index.html")

