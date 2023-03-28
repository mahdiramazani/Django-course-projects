from django.urls import path
from .views import ProfileView,ProfileUser

app_name="Profile_app"
urlpatterns=[

    path("",ProfileView,name="Profile"),
    path("user/<str:name>",ProfileUser,name="Profile_detail"),

]