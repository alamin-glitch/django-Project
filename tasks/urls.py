
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/',views.task_create,name='task_create'),
    path('detail/<int:pk>/',views.task_detail,name='task_detail'),
    path('update/<int:pk>/',views.task_update,name='task_update'),
    path('delete/<int:pk>/',views.task_delete,name='task_delete'),
    path('logout/', views.logout_view, name='logout'),
]