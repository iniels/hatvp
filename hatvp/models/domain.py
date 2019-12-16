from django.db import models
from .related import AutoModel

class Domain(AutoModel):
    __source__ = "hatvp/data/7_domaines_intervention.csv"

    name = models.CharField(max_length=64, verbose_name="domaines_intervention_actions_menees")
    activity = models.ForeignKey(Activity, verbose_name="activite_id")

    def __str__(self):
        return self.name
