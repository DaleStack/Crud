from django.shortcuts import render, redirect
from .forms import NoteModelForm
from .models import NoteModel
# Create your views here.


def create_note(request):
    if request.method == "POST":
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteModelForm()

    return render(request, "crud/create_note.html", {'form':form})

def list_note(request):
    notes = NoteModel.objects.all()

    return render(request, "crud/list_note.html", {'notes':notes})

def update_note(request, pk):
    note = NoteModel.objects.get(id=pk)
    if request.method == "POST":
        form = NoteModelForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteModelForm(instance=note)
    
    return render(request, "crud/update_note.html", {'form':form})

def delete_note(request, pk):
    note = NoteModel.objects.get(id=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')

    return redirect('note_list')
    
