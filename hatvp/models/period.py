from django.db import models
from .information import GeneralInformation

class Period(models.Model):
    __source__ = "hatvp/data/15_exercices.csv"

    id = models.IntegerField(primary_key=True, verbose_name="exercices_id")
    representant = models.ForeignKey(GeneralInformation, verbose_name="representants_id", on_delete=models.CASCADE)
    incomplete_declaration = models.BooleanField(verbose_name="declaration_incomplete", default=False)

    publication = models.DateField(verbose_name="date_publication", blank=True, null=True)

    amount = models.CharField(max_length=128, verbose_name="montant_depense")
    min_amount = models.FloatField(verbose_name="montant_depense_inf")
    max_amount = models.FloatField(verbose_name="montant_depense_sup")
    no_activity = models.BooleanField(verbose_name="exercice_sans_activite", default=False)
    nb_activities = models.PositiveIntegerField(verbose_name="nombre_activites", default=0)

    start = models.DateField(verbose_name="date_debut", blank=True, null=True)
    end = models.DateField(verbose_name="date_fin", blank=True, null=True)
    start_year = models.PositiveIntegerField(verbose_name="annee_debut")
    end_year = models.PositiveIntegerField(verbose_name="annee_fin")

    nb_employees = models.FloatField(verbose_name="nombre_salaries", default=0)

    no_turnover = models.BooleanField(verbose_name="exercice_sans_CA", default=False)
    turnover = models.CharField(max_length=128, verbose_name="chiffre_affaires")
    min_turnover = models.FloatField(verbose_name="ca_inf")
    max_turnover = models.FloatField(verbose_name="ca_sup")

    def __str__(self):
        return "{} {}-{}".format(self.representant, self.start, self.end)
