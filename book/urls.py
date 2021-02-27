from django.urls import path
from . import views

# set the application namespace (helps if we have lots of apps in the future)
app_name = 'book'
urlpatterns = [
    # name is what is used by the {% url %} template tag
    # ex: /book/
    path('', views.index, name='index'),
    # ex: /book/search
    path('search/', views.search, name='search'),
    # ex: /book/5
    path('<int:recipe_id>/', views.detail, name='detail'),
]