from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('feedback/', views.feedback, name='feedback'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('feedback/', views.feedback, name='feedback'),
    path('reg/', views.reg, name='reg'),
    path('acc/', views.acc, name='acc'),
] 

