from django import forms
from .models import Turma, Atividade

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome'] 

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['nome'] 