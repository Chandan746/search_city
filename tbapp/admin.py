from django.contrib import admin
from .models import Country,Cities,Sector,SubSector

class CitiesAdmin(admin.TabularInline):
    model = Cities
class CountryAdmin(admin.ModelAdmin):
    inlines = [CitiesAdmin,]


class SubSectorAdmin(admin.TabularInline):
    model = SubSector
class SectorAdmin(admin.ModelAdmin):
    inlines = [SubSectorAdmin,]



admin.site.register(Country,CountryAdmin)
# admin.site.register(Cities)
admin.site.register(Sector,SectorAdmin)
# admin.site.register(SubSector)
# Register your models here.
