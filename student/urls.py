from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', views.index),
    path('courses/', views.courses),
    path('lectures/', views.lectures),
    path('task/', views.task),
    path('enotes/', views.enotes),
    path('softwarekit/', views.softwarekit),
    path('profile/', views.profile),
    path('logout/', views.logout),
    path('liveclass/', views.liveclass),
    path('ldetails/', views.ldetails),
]
