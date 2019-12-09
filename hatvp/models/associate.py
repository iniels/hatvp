from django.db import models
from .related import RelatedInformation

class Associate(RelatedInformation):
    __source__ = "hatvp/data/3_collaborateurs.csv"

    civility = models.CharField(max_length=8, verbose_name="civilite_collaborateur")
    function = models.CharField(max_length=256, verbose_name="fonction_collaborateur")
    lastname = models.CharField(max_length=64, verbose_name="nom_collaborateur")
    firstname = models.CharField(max_length=64, verbose_name="prenom_collaborateur")
