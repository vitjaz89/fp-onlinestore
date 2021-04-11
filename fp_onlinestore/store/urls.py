
from django.urls import path
from .views import test_view, NotebookDetailView, NotebookListView, SmartphoneListView, SmartphoneDetailView
from .views import SmartphoneCreateView, NotebookCreateView, NotebookDeleteView, SmartphoneDeleteView
from .views import SmartphoneUpdateView, NotebookUpdateView
urlpatterns = [
    path('', test_view, name='base'),
    path('notebooks/<int:pk>', NotebookDetailView.as_view(), name='notebook_detail'),
    path('notebooks', NotebookListView.as_view(), name='notebook_list'),
    path('smartphones', SmartphoneListView.as_view(), name='smartphone_list'),
    path('smartphones/<int:pk>', SmartphoneDetailView.as_view(), name='smartphone_detail'),
    path('notebooks/create/', NotebookCreateView.as_view(), name='notebook_create'),
    path('smartphones/create/', SmartphoneCreateView.as_view(), name='smartphone_create'),
    path('notebooks/<int:pk>/delete', NotebookDeleteView.as_view(), name='notebook_delete'),
    path('smartphones/<int:pk>/delete', SmartphoneDeleteView.as_view(), name='smartphone_delete'),
    path('notebooks/<int:pk>/update', NotebookUpdateView.as_view(), name='notebook_update'),
    path('smartphones/<int:pk>/update', SmartphoneUpdateView.as_view(), name='smartphone_update'),

]

