from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.test),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
     path('service/',views.service,name="service"),
]
