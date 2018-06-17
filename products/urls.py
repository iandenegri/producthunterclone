from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('upvote/<int:product_id>', views.upvote, name='upvote')
]
