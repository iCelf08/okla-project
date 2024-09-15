from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    category = models.CharField(max_length=255)
    instructions = models.TextField()

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_recipe_id = models.CharField(max_length=255)


