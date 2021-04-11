from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Notebook, Smartphone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


def test_view(request):
    return render(request, 'base.html', {})


class NotebookDetailView(DetailView):
    template_name = 'notebook_detail.html'
    model = Notebook
    context_object_name = 'notebook'

class SmartphoneDetailView(DetailView):
    template_name = 'smartphone_detail.html'
    model = Smartphone
    context_object_name = 'smartphone'



class NotebookListView(ListView):
    template_name = 'notebook_list.html'
    model = Notebook
    context_object_name = 'notebooks'

    def get_queryset(self):

        notebooks = Notebook.objects.all()

        return notebooks

class SmartphoneListView(ListView):
    template_name = 'smartphone_list.html'
    model = Smartphone
    context_object_name = 'smartphones'

    def get_queryset(self):

        smartphones = Smartphone.objects.all()

        return smartphones

class NotebookCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['store.add_notebook']
    template_name = 'notebook_create.html'
    model = Notebook
    fields = '__all__'
    success_url = reverse_lazy('notebooks_list')

class SmartphoneCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['store.add_smartphone']
    template_name = 'smartphone_create.html'
    model = Smartphone
    fields = '__all__'
    success_url = reverse_lazy('smartphones_list')

class NotebookDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['store.delete_notebook']
    template_name = 'notebook_delete.html'
    model = Notebook
    context_object_name = 'notebook'
    success_url = reverse_lazy('notebook_list')

class SmartphoneDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['store.delete_smartphone']
    template_name = 'smartphone_delete.html'
    model = Smartphone
    context_object_name = 'smartphone'
    success_url = reverse_lazy('smartphone_list')