from django.db import models
from .information import GeneralInformation

class RelatedInformation(models.Model):
    class Meta:
        abstract = True
    
    id = models.AutoField(primary_key=True)
    representant = models.ForeignKey(GeneralInformation, verbose_name="representants_id", on_delete=models.CASCADE)
    
    def __str__(self):
        return " ".join([self.civility, self.firstname, self.lastname]).strip()
