from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
# from django.template import loader
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from django.contrib import messages

from .models import Recipe, Ingredient

class IndexView(generic.ListView):
    template_name = 'book/index.html'
    context_object_name = 'alpha_recipe_list'

    def get_queryset(self):
        """Return all recipes in alpha order."""
        return Recipe.objects.order_by('title')

def index(request):
    alpha_recipe_list = Recipe.objects.order_by('title')
    # output = ', '.join([r.steps for r in alpha_recipe_list])
    # return HttpResponse(output)
    # template = loader.get_template('book/index.html')
    context = {
        'alpha_recipe_list': alpha_recipe_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'book/index.html', context) # returns an HttpR with rendered template and context

class SearchResultsView(ListView):
    model = Ingredient
    template_name = 'book/search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['ingredient_name'] = self.request.GET['ingredient_name']
        context['num_recipes'] = context['recipe_list'].count()
        return context
    
    def get_queryset(self):
        ingredient_name = self.request.GET['ingredient_name']
        #ingredient = Ingredient.objects.filter(name=ingredient_name)
        recipe_list = Recipe.objects.filter(ingredients__name=ingredient_name).order_by('title')
        return recipe_list

def search(request):
    # ingredient = get_object_or_404(Question, pk=question_id)
    try:
        ingredient_name = request.POST['ingredient_name']
        ingredient = Ingredient.objects.get(name=ingredient_name)
        get_list_or_404(ingredient.recipe_set) #title='Matilda')
    except (KeyError, Ingredient.DoesNotExist):
        # Redisplay the search page.
        return render(request, 'book/index.html', {
            'error_message': "That ingredient didn't exist.",
        })
    else:
        #selected_choice.votes += 1
        #selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('book:search', args=(question.id,)))



    alpha_recipe_list = Recipe.objects.order_by('title')[:5]
    # output = ', '.join([r.steps for r in alpha_recipe_list])
    # return HttpResponse(output)
    # template = loader.get_template('book/index.html')
    print("COUNT: ", + alpha_recipe_list.count())
    context = {
        'alpha_recipe_list': alpha_recipe_list,
        'num_ingredients': alpha_recipe_list.count(),
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'book/search.html', context)

class RecipeDetailView(DetailView):
    """ Show details of recipe and handle 'Try Recipe' button submission. """
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)

        recipe = self.object
        ingredients_list = recipe.ingredients.through.objects.all().filter(recipe=recipe)
        notes_list = recipe.note_set.all()

        # Steps looks like "Boil Water.+Set oven to 450.+Chop all vegetables."
        steps = recipe.steps
        steps_listed = steps.split("+")
        context = {
            'recipe': recipe,
            'steps': steps_listed,
            'ingredients': ingredients_list,
            'notes': notes_list,
        }
        return context

    # If Try Recipe button is pressed, update recipe tries and return to home page with success
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #form = self.get_form()
        messages.success(request, f'{self.object.title} recipe has been tried!')
        self.object.tries += 1
        self.object.save()
        return redirect('book:index')



