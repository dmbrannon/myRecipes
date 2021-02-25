from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Recipe

def index(request):
    alpha_recipe_list = Recipe.objects.order_by('title')[:5]
    # output = ', '.join([r.steps for r in alpha_recipe_list])
    # return HttpResponse(output)
    template = loader.get_template('book/index.html')
    context = {
        'alpha_recipe_list': alpha_recipe_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, recipe_id):
    return HttpResponse(f"You're looking at recipe {recipe_id}.")
