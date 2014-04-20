from django.db import models
from localflavor.us.models import PhoneNumberField

from cyndiloza.apps.places.models import Place


class Person(models.Model):
    first_name = models.CharField("first name", max_length=250)
    last_name = models.CharField("last name", max_length=250)
    nickname = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=250)
    organization = models.CharField(max_length=255, blank=True, help_text="A comma-separated list of membership in organizations or school clubs.")
    place = models.ForeignKey(Place)
    birth = models.DateField(blank=True, null=True, help_text="Written in YYYY-MM-DD")
    death = models.DateField(blank=True, null=True, help_text="Written in YYYY-MM-DD")
    photo = models.ImageField(upload_to="people/", blank=True)
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True)
    url = models.URLField("URL", blank=True)
    characteristic = models.TextField(blank=True, help_text="Something memorable about this person.")

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name_plural = "people"

    def __unicode__(self):
        return u"%s %s, %s" % (self.first_name, self.last_name, self.title)
