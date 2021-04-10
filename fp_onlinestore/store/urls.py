
from django.urls import path
from .views import test_view, ProductDetailView, NotebookListView, SmartphoneListView

urlpatterns = [
    path('', test_view, name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('notebooks', NotebookListView.as_view(), name='notebook_list'),
    path('smartphones', SmartphoneListView.as_view(), name='smartphone_list')



]

