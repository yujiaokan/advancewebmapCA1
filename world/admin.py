from django.contrib.gis import admin
from .models import WorldBorder, Profile



admin.site.register(WorldBorder, admin.OSMGeoAdmin)


