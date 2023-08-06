from django.urls import path
from recipes.views import show_recipe, recipe_list, create_recipe, edit_recipe, about


urlpatterns = [
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
    path("recipes/", recipe_list, name="main_page"),
    path("recipes/create/", create_recipe, name="create_recipe"),
    path("recipes/edit/<int:id>/", edit_recipe, name="edit_recipe"),
    # path("recipes/delete/<int:id>/", edit_recipe, name="delete_recipe"),
    path("recipes/about/", about, name="about"),
]
