"""day007 URL Configuration

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
from django.urls import path, re_path
from project import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('class_list/', views.class_list, name="class_list"),
    path('delete_class/', views.delete_class, name="delete_class"),
    path('add_class/', views.add_class, name="add_class"),
    re_path('edit_class/(\d+)/', views.edit_class, name="edit_class"),

    re_path('student_list/', views.student_list, name="student_list"),
    path('add_student/', views.add_student, name="add_student"),
    path('delete_student/', views.delete_student, name="delete_student"),
    re_path('edit_student/(\d+)/', views.edit_student, name="edit_student"),

    path('teacher_list/', views.teacher_list, name="teacher_list"),
    re_path('delete_teacher/(\d+)/', views.delete_teacher, name="delete_teacher"),
    path('add_teacher/', views.add_teacher, name="add_teacher"),
    re_path('edit_teacher/(\d+)/', views.edit_teacher, name="edit_teacher"),

    path('school/', views.school, name="school"),
]
