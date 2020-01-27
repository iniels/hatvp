from django.db import models
from .information import GeneralInformation
    
class Action(models.Model):
    __source__ = "hatvp/data/10_actions_menees.csv"

    id = models.IntegerField(primary_key=True, verbose_name="action_representation_interet_id")
    
    def __str__(self):
        return self.id

class TypeAction(models.Model):
    __source__ = "hatvp/data/10_actions_menees.csv"

    desc = models.TextField(verbose_name="action_menee")
    action = models.ForeignKey(Action, verbose_name="action_representation_interet_id", on_delete=models.CASCADE)
    more = models.TextField(verbose_name="action_menee_autre")

    def __str__(self):
        return self.desc
