from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('save/', views.saveUser , name='save'),
    path('detele/', views.deleteUser , name='delete'),
    path('edit/', views.editUser, name='edit'),
]