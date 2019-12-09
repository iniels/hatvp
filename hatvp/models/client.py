from django.db import models
from .related import RelatedInformation

class Client(RelatedInformation):
    __source__ = "hatvp/data/4_clients.csv"

    name = models.CharField(max_length=256, verbose_name="denomination_client")
    nif = models.CharField(max_length=16, verbose_name="identifiant_national_client")
    nif_type = models.CharField(max_length=16, verbose_name="type_identifiant_national_client")

    def __str__(self):
        return self.name
