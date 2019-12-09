from django.contrib import admin
from .models import GeneralInformation, Affiliation, Director, Associate, Client, Level, Period

admin.site.register(GeneralInformation)
admin.site.register(Affiliation)
admin.site.register(Director)
admin.site.register(Associate)
admin.site.register(Client)
admin.site.register(Level)
admin.site.register(Period)
