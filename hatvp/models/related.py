from django.db import models
from .information import GeneralInformation
from .period import Period

class AutoModel(models.Model):
    class Meta:
        abstract = True
        
    id = models.AutoField(primary_key=True)

class RelatedInformation(AutoModel):
    class Meta:
        abstract = True
    
    representant = models.ForeignKey(GeneralInformation, verbose_name="representants_id", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.representant)
