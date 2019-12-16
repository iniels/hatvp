from django.db import models
from .related import RepresentantRelatedModel

class Field(RelatedInformation):
    __source__ = "hatvp/data/9_secteurs_activites.csv"

    name = models.CharField(max_length=64, verbose_name="secteur_activite")

    def __str__(self):
        return self.name
