from django.db import models
from .period import Period

class Activity(models.Model):
    __source__ = "hatvp/data/8_objets_activites.csv"
    class Meta:
        verbose_name_plural = "Activities"
    
    id = models.IntegerField(verbose_name="activite_id", primary_key=True)
    period = models.ForeignKey(Period, verbose_name="exercices_id", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="date_publication_activite", blank=True, null=True)
    ref = models.CharField(max_length=8, verbose_name="identifiant_fiche")
#    desc = models.TextField(verbose_name="objet_activite", blank=True, null=True)

    def __str__(self):
        return self.ref
