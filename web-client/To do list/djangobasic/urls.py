"""djangobasic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blogs import views
from blogs.views import TaskDetail, TaskList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello),
   # path('task/<int:pk>',TaskDetail.as_view(),name='tasks'),
    path('page1',views.page1),
    path('createForm',views.createForm),
    path('addForm',views.addUser),
    path('loginForm',views.loginForm),
    path('login',views.login),
    path('logout',views.logout),
    path('addForm',views.addTodo)
]
