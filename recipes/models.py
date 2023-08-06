from django.db import models

from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField(blank=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# I added this following the exploration
# along with the import and variable up above
    author = models.ForeignKey(
        USER_MODEL,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True,
    )


class RecipeStep(models.Model):
    step_number = models.PositiveSmallIntegerField()
    instruction = models.TextField()

    recipe = models.ForeignKey(
        Recipe,
        related_name='steps',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['step_number']


class RecipeIngredient(models.Model):
    amount = models.CharField(max_length=150)
    food_item = models.CharField(max_length=150)

    recipe = models.ForeignKey(
        Recipe,
        related_name='ingredients',
        on_delete=models.CASCADE,
    )
