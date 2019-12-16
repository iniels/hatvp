import csv
from datetime import datetime
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from hatvp.models import GeneralInformation, Affiliation, Director, Associate, Client, Level, Period, Activity

class Command(BaseCommand):
    help = ''

    def import_csv(self, cls):
        with open(cls.__source__, "rU") as src:
            print("Importing '{}' ... ".format(cls._meta.object_name), end='')
            reader = csv.reader(src, delimiter=';', quotechar='"')
            header = next(reader)
            cols = {}
            for pos, label in enumerate(header):
                cols[label] = pos
            # print(cols)
            cnt = 0
            for row in reader:
                if int(row[0]) < 10506:
                    continue
                print(row[0])
                defaults = {}
                for field in cls._meta.fields:
                    if isinstance(field, models.AutoField):
                        defaults["id"] = None
                        continue
                    value = row[cols[field.verbose_name]]
                    if value:
                        if isinstance(field, models.DateTimeField):
                            try:
                                defaults[field.attname] = datetime.strptime(value, "%d/%m/%Y %H:%M:%S")
                            except:
                                defaults[field.attname] = datetime.strptime(value, "%Y-%m-%d")
                        else:
                            defaults[field.attname] = value
                cls.objects.update_or_create(defaults, pk=defaults["id"])
                cnt += 1
                # if cnt == 20:
                #    break
            print("done")
            
    def handle(self, *args, **options):
#        self.import_csv(GeneralInformation)
#        self.import_csv(Director)
#        self.import_csv(Associate)
#        self.import_csv(Client)
#        self.import_csv(Affiliation)
#        self.import_csv(Level)
#        self.import_csv(Period)
        self.import_csv(Activity)
#        self.import_csv(Domain)
#        self.import_csv(Field)
#        self.import_csv(Action)
#        self.import_csv(Beneficiary)
#        self.import_csv(Decision)
#        self.import_csv(Target)
#        self.import_csv(Observation)
