from django.urls import path
from .views import ProfileView

urlpatterns=[

    path("",ProfileView)
]

