from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader

from .models import Recipe

def index(request):
    alpha_recipe_list = Recipe.objects.order_by('title')[:5]
    # output = ', '.join([r.steps for r in alpha_recipe_list])
    # return HttpResponse(output)
    # template = loader.get_template('book/index.html')
    context = {
        'alpha_recipe_list': alpha_recipe_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'book/index.html', context) # returns an HttpR with rendered template and context

def search(request):
    alpha_recipe_list = Recipe.objects.order_by('title')[:5]
    # output = ', '.join([r.steps for r in alpha_recipe_list])
    # return HttpResponse(output)
    # template = loader.get_template('book/index.html')
    context = {
        'alpha_recipe_list': alpha_recipe_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'book/search.html', context)

def detail(request, recipe_id):
    '''try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist.")'''
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    
    # Steps looks like "Boil Water.  Set oven to 450.  Chop all vegetables."
    steps = recipe.steps
    steps_listed = steps.split("  ")
    context = {
        'recipe': recipe,
        'steps': steps_listed,
    }
    
    return render(request, 'book/detail.html', context)
