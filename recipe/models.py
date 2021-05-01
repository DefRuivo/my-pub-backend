from django.db import models


class Ingredient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey("core.Product", on_delete=models.CASCADE)
