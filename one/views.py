from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note
# Create your views here.

class NoteListView(ListView):
    model = Note
    template_name = 'one/note_list.html'
    context_object_name = 'notes'
    ordering = ['-updated_at']

class NoteCreateView(CreateView):
    model = Note
    template_name = 'one/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('one:note_list')

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'one/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('one:note_list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'one/note_confirm_delete.html'
    success_url = reverse_lazy('one:note_list')

