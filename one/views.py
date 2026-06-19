from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # Import the mixin
from .models import Note

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'one/note_list.html'
    context_object_name = 'notes'
    
    # Override to only show notes for the logged-in user
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-updated_at')

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'one/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('one:note_list')

    # Override to automatically assign the logged-in user to the new note
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'one/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('one:note_list')

    # Ensure a user can only edit their own notes (prevents URL guessing)
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'one/note_confirm_delete.html'
    success_url = reverse_lazy('one:note_list')

    # Ensure a user can only delete their own notes
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)