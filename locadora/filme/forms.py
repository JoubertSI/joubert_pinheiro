from django import forms
from .models import Filmes

class FilmeForms (forms.ModelForm):
    class Meta:
        model = Filmes
        fields = '__all__'#Importando os Campos da Classe Filmes