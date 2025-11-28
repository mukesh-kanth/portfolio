"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_page',views.admin_page,name='admin_page'),
    path('project_list', views.project_list, name='project_list'),
    path('projects/add/', views.project_create, name='project_create'),
    path('projects/<int:pk>/edit/', views.project_update, name='project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('skill_list', views.skill_list, name='skill_list'),
    path('skills/add/', views.skill_create, name='skill_create'),
    path('skills/<int:pk>/edit/', views.skill_update, name='skill_update'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    path('profile_list', views.profile_list, name='profile_list'),
    path('profiles/add/', views.profile_create, name='profile_create'),
    path('profiles/<int:pk>/edit/', views.profile_update, name='profile_update'),
    path('profiles/<int:pk>/delete/', views.profile_delete, name='profile_delete'),
    path('experience/', views.experience_list, name='experience_list'),
    path('experience/add/', views.add_experience, name='add_experience'),
    path('experience/edit/<int:exp_id>/', views.edit_experience, name='edit_experience'),
    path('experience/delete/<int:exp_id>/', views.delete_experience, name='delete_experience'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('contact-list/', views.contact_list_view, name='contact_list_view'),
]
