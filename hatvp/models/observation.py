from django.db import models
from .related import AutoModel
from .information import GeneralInformation
from .activity import Activity

class Target(AutoModel):
    __source__ = "hatvp/data/14_observations.csv"

    representant = models.ForeignKey(GeneralInformation, verbose_name="action_representation_interet_id", on_delete=models.CASCADE)
    activity = models.CharField(max_length=128, verbose_name="activite_id")
    observation = models.TextField(verbose_name="observation")

    def __str__(self):
        return self.observation[:32]
