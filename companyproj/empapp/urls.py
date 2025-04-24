# filepath: c:\Users\96550\Documents\GitHub\lab-final-Yousef2212176134\companyproj\empapp\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees, name='employees'),
    path('create/', views.create_employee, name='create_employee'),
    path('update/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
]