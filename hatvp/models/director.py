from django.db import models
from .related import RelatedInformation

class Director(RelatedInformation):
    __source__ = "hatvp/data/2_dirigeants.csv"

    civility = models.CharField(max_length=8, verbose_name="civilite_dirigeant")
    function = models.CharField(max_length=256, verbose_name="fonction_dirigeant")
    lastname = models.CharField(max_length=64, verbose_name="nom_dirigeant")
    firstname = models.CharField(max_length=64, verbose_name="prenom_dirigeant")
