from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),   
    path('completed', views.completed, name= 'completed'),   
    path('details/<str:id>', views.details, name= 'details'),
    path('create/', views.create, name='create'),   
    path('update/<str:id>', views.update, name= 'update'),
    path('delete/<str:id>', views.delete, name= 'delete'),
    path('signup/', views.signup, name= 'signup'),
    path('signin/', views.signin, name= 'signin'),
    path('signout/', views.signout, name= 'signout'),

]