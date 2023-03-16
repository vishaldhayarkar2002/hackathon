# manually created
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('xray', views.xray, name = 'xray'),
    path('register', views.register,name='register'),
    path('doctorLogin', views.doctorLogin, name='doctorLogin'),
    path('patientLogin', views.patientLogin,name='patientLogin'),
    path('logout', views.logout,name='logout'),
    # path('success', views.success, name='success'),
    path('xray/upload', views.image_upload_view)
]
