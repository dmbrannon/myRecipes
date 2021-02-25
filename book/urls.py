from django.urls import path
from . import views

urlpatterns = [
    # ex: /book/
    path('', views.index, name='index'),
    # ex: /book/5
    path('<int:recipe_id>/', views.detail, name='detail'),
]