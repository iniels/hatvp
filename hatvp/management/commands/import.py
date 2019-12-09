import csv
from datetime import datetime
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from hatvp.models import GeneralInformation, Affiliation, Director, Associate, Client, Level

class Command(BaseCommand):
    help = ''

#    def add_arguments(self, parser):
#        parser.add_argument('poll_ids', nargs='+', type=int)

    def import_csv(self, cls):
        with open(cls.__source__) as src:
            print("Importing '{}' ... ".format(cls._meta.object_name), end='')
            reader = csv.reader(src, delimiter=';')
            header = next(reader)
            cols = {}
            for pos, label in enumerate(header):
                cols[label] = pos
            # print(cols)
            cnt = 0
            for row in reader:
                defaults = {}
                for field in cls._meta.fields:
                    if isinstance(field, models.AutoField):
                        defaults["id"] = None
                        continue
                    value = row[cols[field.verbose_name]]
                    if value:
                        if isinstance(field, models.DateTimeField):
                            defaults[field.attname] = datetime.strptime(value, "%d/%m/%Y %H:%M:%S")
                        else:
                            defaults[field.attname] = value
                cls.objects.update_or_create(defaults, pk=defaults["id"])
                cnt += 1
                if cnt == 20:
                    break
            print("done")
            
    def handle(self, *args, **options):
        #self.import_csv(GeneralInformation)
        #self.import_csv(Director)
        #self.import_csv(Associate)
        #self.import_csv(Client)
        self.import_csv(Level)
        #self.import_csv(Affiliation)

