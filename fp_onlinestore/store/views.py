from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Notebook, Smartphone
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
