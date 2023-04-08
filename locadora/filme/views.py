from django.shortcuts import render, redirect
from .models import Filmes
from .forms import FilmeForms

def base(request):
    filme = Filmes
    template_name = 'base.html'
    context = {'filme':filme}
    return render(request, template_name, context)

def filme_list(request):
    filme = Filmes.objects.all()
    template_name = 'filme_list.html'
    context = {'filmes':filme}
    return render(request, template_name, context)

def filme_new(request):
    if request.method == "POST":
     filme_novo = FilmeForms(request.POST)
     if filme_novo.is_valid():
        filme_novo.save()
        return redirect('filme_list')

    else:  
      template_name = 'filme_new.html'
      context = {'form':FilmeForms}
      return render(request, template_name, context)
        
def filme_edit(request, pk):
    edit = Filmes.objects.get(id=pk)
    if request.method == "POST":
      edit = FilmeForms(request.POST,instance=edit)
      if edit.is_valid():
        edit.save()
        return redirect('filme_list')

    else:  
      template_name = 'filme_edit.html'
      context = {'form': FilmeForms(instance= edit),
                 'pk':pk
      }
      return render(request, template_name, context)    

def filme_delete(request,pk):
    filme_delete = Filmes.objects.get(id=pk)
    filme_delete.delete()
    return redirect('filme_list')
        
# Create your views here.




