from django.urls import path
from . import views

app_name = 'one'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note_list'),
    path('create/', views.NoteCreateView.as_view(), name='note_create'),
    path('update/<int:pk>/', views.NoteUpdateView.as_view(), name='note_update'),
    path('delete/<int:pk>/', views.NoteDeleteView.as_view(), name='note_delete'),
]