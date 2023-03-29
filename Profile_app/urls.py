from django.urls import path
from .views import ProfileView,Profile_User

urlpatterns=[

    path("",ProfileView),
    path("user/<str:name>",Profile_User)
]

