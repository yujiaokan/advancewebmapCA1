from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField(srid=4326)
    # Returns the string representation of the model.

    def __str__(self):
        return self.name





class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    location = models.PointField(
        editable=False,
        blank=True,
        null=True,
        default=None)

    def __str__(self):
        return self.user.name, self.lon, self.lat


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Note(models.Model):
    note_heading = models.CharField(max_length=200, blank=True,null=True)
    note = models.CharField(max_length=1000,blank=True,null=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.note_heading





