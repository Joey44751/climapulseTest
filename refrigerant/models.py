from django.db import models
from django.core.validators import MinValueValidator


class Vessel(models.Model):
    name = models.CharField(max_length=100)
    content = (
        models.PositiveIntegerField()
    )  # Amount of refrigerant in the vessel, in kilograms
