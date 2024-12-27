from django.urls import path
from .views import *

urlpatterns = [
    path('index', List_View.as_view(), name='book-list'),
    path('create', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
]