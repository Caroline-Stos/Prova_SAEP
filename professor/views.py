from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import TurmaForm, AtividadeForm
from .models import Professor, Turma, Atividade

class Home(LoginRequiredMixin, View):
    """Página inicial."""
    def get(self, request):
        turmas = Turma.objects.filter(professor__user=request.user) 
        professor = get_object_or_404(Professor, user=request.user)
        return render(request, 'home.html', {'turmas': turmas, 'professor': professor})
    
class CadastrarTurma(LoginRequiredMixin, CreateView):
    """View para cadastrar uma nova turma."""
    model = Turma
    form_class = TurmaForm
    template_name = 'cadastrar.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        professor = get_object_or_404(Professor, user=self.request.user)
        form.instance.professor = professor
        return super().form_valid(form)

class ListarAtividades(LoginRequiredMixin, View):
    """View para listar atividades de uma turma."""
    def get(self, request, pk):
        turma = get_object_or_404(Turma, pk=pk)
        atividades = turma.atividade_set.all()
        professor = get_object_or_404(Professor, user=request.user)
        return render(request, 'listar_atividades.html', {
            'turma': turma, 
            'atividades': atividades, 
            'professor': professor
        })

class CadastrarAtividade(LoginRequiredMixin, CreateView):
    """View para cadastrar uma nova atividade."""
    model = Atividade
    form_class = AtividadeForm
    template_name = 'cadastrar.html'

    def form_valid(self, form):
        turma = get_object_or_404(Turma, id=self.kwargs['pk'])
        form.instance.turma = turma
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('listar_atividades', kwargs={'pk': self.kwargs['pk']})

class DeletarTurma(LoginRequiredMixin, DeleteView):
    """View para deletar uma turma."""
    model = Turma
    template_name = 'confirmar_exclusao.html'  
    success_url = reverse_lazy('home')