from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from planeta.forms import PlanetaForm, ElementoFormSet, UpdateElementoFormSet
from planeta.models import Planeta


class ListPlanetasView(ListView):
    model = Planeta
    context_object_name = 'planetas'
    template_name = 'planeta/list.html'
    ordering = ['nome', 'create_at']


class CreatePlanetaView(CreateView):
    form_class = PlanetaForm
    template_name = 'planeta/create.html'
    success_url = reverse_lazy('planeta-create')

    def get_context_data(self, **kwargs):       
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['elemento'] = ElementoFormSet(self.request.POST)
        else:
            data['elemento'] = ElementoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        elemento = context['elemento']
        self.object = form.save()
        if elemento.is_valid():
            elemento.instance = self.object
            elemento.save()
            messages.success(self.request, 'Planeta salvo com sucesso.')
        return super().form_valid(form)


class PlanetaDetailView(DetailView):
    model = Planeta
    template_name = 'planeta/detail.html'
    context_object_name = 'planeta'


class PlanetaDeleteView(DeleteView):
    model = Planeta
    context_object_name = 'planeta'
    template_name = 'planeta/delete.html'
    success_url = reverse_lazy('planeta-home')

    def form_valid(self, form):
        messages.success(self.request, 'Planeta deletado com sucesso.')
        return super().form_valid(form)


class UpdatePlanetaView(UpdateView):
    model = Planeta
    form_class = PlanetaForm
    template_name = 'planeta/update.html'
    success_url = reverse_lazy('planeta-home')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['elemento'] = UpdateElementoFormSet(self.request.POST, instance=self.object)
        else:
            data['elemento'] = UpdateElementoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        elemento = context['elemento']
        for formset in elemento.forms:
            if formset.is_valid():
                formset.save()
            else:
                messages.error(self.request, 'Ocorreu um erro ao salvar os novos dados.')
        messages.success(self.request, 'Os novos dados foram salvos com sucesso.')
        return super().form_valid(form)
