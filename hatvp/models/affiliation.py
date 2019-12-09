from django.db import models
from .related import RelatedInformation

class Affiliation(RelatedInformation):
    __source__ = "hatvp/data/5_affiliations.csv"

    name = models.CharField(max_length=256, verbose_name="denomination_affiliation")
    nif = models.CharField(max_length=16, verbose_name="identifiant_national_affiliation")
    nif_type = models.CharField(max_length=16, verbose_name="type_identifiant_national_affiliation")

    def __str__(self):
        return self.name
