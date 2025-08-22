from django.urls import path
from .views import create_note, list_note, update_note, delete_note

urlpatterns = [
    path('create/', create_note, name='create_note'),
    path('list/', list_note, name='list_note'),
    path('update/<int:pk>/', update_note, name='update_note'),
    path('delete/<int:pk>/', delete_note, name='delete_note'),
]
