from email import message
from turtle import title
from django.shortcuts import render
# from .models import Notes
from .forms import *
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'dashboard/home.html')


def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(
                user=request.user, title=request.POST['title'], description=request.POST['description'])
            notes.save()
        messages.success(
            request, f'вы успешно добавили {request.user.username} новую задачу!')
    else:

        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'dashboard/notes.html', context)
