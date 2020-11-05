from django.urls import path
from . import views

urlpatterns = [path('', views.post_list, name='post_list'),
               path('list/', views.index, name='index'),
               path('list/new/', views.new, name='new'),
               path('students/', views.indexStudents, name='indexStudents'),
               path('students/create/', views.create, name='create'),
               path('students/edit/<id>/', views.edit, name='edit'),
               path('students/delete/<id>/', views.delete, name='create'), ]
