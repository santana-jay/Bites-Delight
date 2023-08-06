from django.contrib import admin
from recipes.models import Recipe, RecipeStep

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
    )


@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        'step_number',
        'instruction',
        'id',
    )
