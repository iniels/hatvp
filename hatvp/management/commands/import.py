import zipfile
import csv
from datetime import datetime
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from hatvp.models import GeneralInformation, Affiliation, Director, Associate, Client, Level, Period, Activity

class Command(BaseCommand):
    help = 'Import HATVP data from models and CSV files'

    def import_csv(self, cls):
        ''' 
        From a hatvp model, reads a csv file and find data using
        introspection. The trick is the use of 'verbose_name' as
        the name of the column to retrieve in the file
        '''
        with open(cls.__source__, "rU") as src:
            print("Importing '{}' ... ".format(cls._meta.object_name), end='')
            reader = csv.reader(src, delimiter=';', quotechar='"')
            header = next(reader)
            cols = {}
            # get column indexes for each column name
            # makes it easy to find data from names
            for pos, label in enumerate(header):
                cols[label] = pos

            cnt = 0
            for row in reader:
                # print(row[0]) # debug

                # prepare a dict for 'update_or_create'
                defaults = {}

                # parse all fields from the model and set them
                for field in cls._meta.fields:
                    # if the field is an AutoField, it is not found
                    # in the CSV file, so ignore it (auto increment)
                    if isinstance(field, models.AutoField):
                        defaults["id"] = None
                        continue
                    # get value in the CSV file
                    value = row[cols[field.verbose_name]]
                    if value:
                        # if the field is a date time, try to
                        # parse it according to the 'manually'
                        # detected formats
                        if isinstance(field, models.DateTimeField):
                            try:
                                defaults[field.attname] = datetime.strptime(value, "%d/%m/%Y %H:%M:%S")
                            except ValueError: # strptime raises a ValueError
                                defaults[field.attname] = datetime.strptime(value, "%Y-%m-%d")
                        # else, simply set the field
                        else:
                            defaults[field.attname] = value
                # update or create an instance
                cls.objects.update_or_create(defaults, pk=defaults["id"])
                cnt += 1
            print("done {} records".format(cnt))
            
    def handle(self, *args, **options):
        '''
        import data in the correct order
        '''
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
