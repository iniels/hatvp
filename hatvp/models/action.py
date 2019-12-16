from django.db import models
from .information import GeneralInformation

class Action(models.Model):
    __source__ = "hatvp/data/10_actions_menees.csv"

    desc = models.TextField(verbose_name="action_menee")
    representant = models.ForeignKey(GeneralInformation, verbose_name="action_representation_interet_id", on_delete=models.CASCADE)
    more = models.TextField(verbose_name="action_menee_autre")

    def __str__(self):
        return self.desc
