from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import TurmaForm, AtividadeForm
from .models import Professor, Turma, Atividade

class Home(LoginRequiredMixin, View):
    def get(self, request):
        turmas = Turma.objects.all()
        professor = Professor.objects.get(user=self.request.user)
        return render(request, 'home.html', {'turmas': turmas, 'professor': professor})
    
class CadastrarTurma(LoginRequiredMixin, CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'cadastrar.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        professor = Professor.objects.get(user=self.request.user)
        form.instance.professor = professor
        return super().form_valid(form)

class ListarAtividades(LoginRequiredMixin, View):
    def get(self, request, pk):
        turma = get_object_or_404(Turma, pk=pk)
        atividades = Atividade.objects.filter(turma=turma)
        professor = get_object_or_404(Professor, user=request.user)
        return render(request, 'listar_atividades.html', {
            'turma': turma, 
            'atividades': atividades, 
            'professor': professor
        })

class CadastrarAtividade(LoginRequiredMixin, CreateView):
    model = Atividade
    form_class = AtividadeForm
    template_name = 'cadastrar.html'
    success_url = reverse_lazy('listar_atividades')

    def form_valid(self, form):
        turma = get_object_or_404(Turma, id=self.kwargs['pk'])
        form.instance.turma = turma
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listar_atividades', kwargs={'pk': self.kwargs['pk']})

class DeletarTurma(LoginRequiredMixin, DeleteView):
    model = Turma
    template_name = 'confirmar_exclusao.html'  # Seu template de confirmação de exclusão
    success_url = reverse_lazy('home')