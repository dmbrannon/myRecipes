"""myRecipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path() is passed route and view (and kwargs and name are optional)
    # the route is the end of the url (minus GET/POST params)
    # django calls the specified view function with an HttpRequest obj and captured values from url as args
    # name is so we can refer to it in templates in our project
    path('', include('book.urls')), # include lets us reference the other url modules! use it for everything 
    path('admin/', admin.site.urls),
]
