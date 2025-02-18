from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/', views.edit_post, name='edit_post'),
    path('delete_post/', views.delete_post, name='delete_post'),
]
