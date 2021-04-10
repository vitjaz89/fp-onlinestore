from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Notebook, Smartphone
# Create your views here.


def test_view(request):
    return render(request, 'base.html', {})


class ProductDetailView(DetailView):
    CT_MODEL_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)


    #model = Model
    #queryset = Model.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

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
