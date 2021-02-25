from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('todos/',views.todos,name='todos'),
  path('taskcomplete/',views.taskcomplete,name='taskcomplete'),
  path('deletetask/',views.deletetask,name='deletetask'),
  path('login/',views.loginpage,name='login'),
  path('logout/',views.logoutpage,name='logout'),
  path('register/',views.registerpage,name='register'),
]