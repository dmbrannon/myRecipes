from django.urls import path
# from book.views import SearchResultsView

from . import views

# set the application namespace (helps if we have lots of apps in the future)
app_name = 'book'
urlpatterns = [
    # name is what is used by the {% url %} template tag
    # ex: /book/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /book/search
    path('search/', views.SearchResultsView.as_view(), name='search'),
    # ex: /book/5
    path('<int:recipe_id>/', views.detail, name='detail'),
]