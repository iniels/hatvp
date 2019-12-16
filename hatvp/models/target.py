from django.db import models
from .related import AutoModel
from .information import GeneralInformation

class Target(AutoModel):
    __source__ = "hatvp/data/13_ministeres_aai_api.csv"

    representant = models.ForeignKey(GeneralInformation, verbose_name="action_representation_interet_id", on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name="responsable_public")
    department = models.CharField(max_length=128, verbose_name="departement_ministeriel")
    more = models.CharField(max_length=128, verbose_name="responsable_public_ou_dpt_ministeriel_autre")

    def __str__(self):
        return self.name
