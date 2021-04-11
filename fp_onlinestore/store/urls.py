
from django.urls import path
from .views import test_view, NotebookDetailView, NotebookListView, SmartphoneListView

urlpatterns = [
    path('', test_view, name='base'),
    path('notebooks/<int:pk>', NotebookDetailView.as_view(), name='notebook_detail'),
    path('notebooks', NotebookListView.as_view(), name='notebook_list'),
    path('smartphones', SmartphoneListView.as_view(), name='smartphone_list')



]

