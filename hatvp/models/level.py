from django.db import models
from .related import RelatedInformation

class Level(RelatedInformation):
    __source__ = "hatvp/data/6_niveaux_intervention.csv"
    LEVEL_CHOICES = (
        ('1', 'Local'),
        ('2', 'National'),
        ('3', 'Européen'),
        ('4', 'Mondial')
    )
    level = models.CharField(max_length=1, verbose_name="niveau_intervention", choices=LEVEL_CHOICES)

    def __str__(self):
        return "{} au niveau {}".format(self.representant, self.get_level_display())
