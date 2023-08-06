from recipes.models import Recipe, RecipeStep, RecipeIngredient
from django.forms import ModelForm
# from django.views.generic import UpdateView  # type: ignore


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'picture', 'description']


class RecipeStepForm(ModelForm):
    class Meta:
        model = RecipeStep
        fields = ['step_number', 'instruction']


class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['amount', 'food_item']
