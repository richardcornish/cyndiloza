from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.us.models import PhoneNumberField

from cyndiloza.places.models import Place


class Person(models.Model):
    first_name = models.CharField(_("first name"), max_length=250)
    last_name = models.CharField(_("last name"), max_length=250)
    nickname = models.CharField(_("nickname"), max_length=250, blank=True)
    slug = models.SlugField(_("slug"), unique=True)
    title = models.CharField(_("title"), max_length=250)
    organization = models.CharField(_("organization"), max_length=255, blank=True, help_text="A comma-separated list of membership in organizations or school clubs.")
    place = models.ForeignKey(Place)
    birth = models.DateField(_("date of birth"), blank=True, null=True, help_text="Written in YYYY-MM-DD")
    death = models.DateField(_("date of death"), blank=True, null=True, help_text="Written in YYYY-MM-DD")
    photo = models.ImageField(_("photo"), upload_to="people/", blank=True)
    phone = PhoneNumberField(_("phone"), help_text="In the form of XXX-XXX-XXXX.")
    email = models.EmailField(_("email"), blank=True)
    url = models.URLField(_("URL"), blank=True, help_text="Personal website, e.g. Facebook or Twitter.")
    characteristic = models.TextField(_("characteristic"), blank=True, help_text="Something memorable about this person.")

    # email_alert = models.BooleanField("E-mail alerts", default=False)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = _("person")
        verbose_name_plural = _("people")

    def __unicode__(self):
        return u"%s %s, %s" % (self.first_name, self.last_name, self.title)
