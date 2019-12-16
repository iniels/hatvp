from django.db import models
from .related import RepresentantRelatedModel

class Beneficiary(models.Model):
    __source__ = "hatvp/data/11_beneficiaires.csv"

    name = models.CharField(max_length=128, verbose_name="action_menee")
    representant = models.ForeignKey(GeneralInformation, verbose_name="action_representation_interet_id", on_delete=models.CASCADE)
    own = models.BooleanField(verbose_name="action_menee_en_propre", default=False)

    def __str__(self):
        return self.name
