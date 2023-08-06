from django.shortcuts import (
                                render,
                                get_object_or_404,
                                redirect,
                            )
from recipes.models import Recipe, RecipeStep, RecipeIngredient
from recipes.forms import RecipeForm, RecipeStepForm, RecipeIngredientForm
# from django.forms import modelformset_factory, formset_factory


# Create your views here.
def show_recipe(request, id):

    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }

    return render(request, "recipes/detail.html", context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }

    return render(request, "recipes/list.html", context)


def create_recipe(request):
    form = RecipeForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("main_page")

    else:
        form = RecipeForm()

    context = {
        "form": form
    }
    return render(request, 'recipes/create.html', context)


# def edit_recipe(request, id):
#     recipe = get_object_or_404(Recipe, id=id)

#     # step_form = RecipeStepForm(initial={'recipe': recipe})

#     # ingredient_form = RecipeIngredientForm(initial={'recipe': recipe})

#     if request.method == "POST":
#         form = RecipeForm(request.POST, instance=recipe)
#         step_form = RecipeStepForm(initial={'recipe': recipe})
#         ingredient_form = RecipeIngredientForm(initial={'recipe': recipe})

#         if form.is_valid() \
#             and step_form.is_valid() \
#                 and ingredient_form.is_valid():
#             form.save()

#             for step in step_form:
#                 s = step.save(commit=False)
#                 s.recipe = recipe
#                 s.save()

#             for ingredient in ingredient_form:
#                 i = ingredient.save(commit=False)
#                 i.recipe = recipe
#                 i.save()

#             return redirect("show_recipe", id=recipe.id)

#     else:
#         form = RecipeForm(instance=recipe)

#         step_form = RecipeStepForm(initial={'recipe': recipe})

#         ingredient_form = RecipeIngredientForm(initial={'recipe': recipe})

#     context = {
#         "form": form,
#         "step_form": step_form,
#         "ingredient_form": ingredient_form,
#         "recipe": recipe
#     }
#     return render(request, "recipes/edit.html", context)


def about(request):
    return render(request, "recipes/about.html")


def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)

        # Process steps
        steps = []
        for key, value in request.POST.items():
            if key.startswith('step-instruction-'):
                step_number_key = key.replace('instruction', 'count')
                step_number = request.POST.get(step_number_key)
                if value and step_number:
                    steps.append(RecipeStep(recipe=recipe, instruction=value, step_number=step_number))

        # Process ingredients
        ingredients = []
        for key, value in request.POST.items():
            if key.startswith('ingredient-item-'):
                amount_key = key.replace('item', 'amount')
                amount = request.POST.get(amount_key)
                if value and amount:
                    ingredients.append(RecipeIngredient(recipe=recipe, food_item=value, amount=amount))


        if form.is_valid():
            form.save()
            RecipeStep.objects.filter(recipe=recipe).delete()  # Remove existing steps
            RecipeStep.objects.bulk_create(steps)
            RecipeIngredient.objects.filter(recipe=recipe).delete()  # Remove existing ingredients
            RecipeIngredient.objects.bulk_create(ingredients)
            return redirect("show_recipe", id=recipe.id)

    else:
        form = RecipeForm(instance=recipe)
        step_form = RecipeStepForm(initial={'recipe': recipe})
        ingredient_form = RecipeIngredientForm(initial={'recipe': recipe})

    context = {
        "form": form,
        "step_form": step_form,
        "ingredient_form": ingredient_form,
        "recipe": recipe
    }
    return render(request, "recipes/edit.html", context)
