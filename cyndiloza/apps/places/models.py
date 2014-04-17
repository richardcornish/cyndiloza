from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from localflavor.us.us_states import US_STATES

import re


class District(models.Model):
    name = models.CharField(_("name"), max_length=250)
    slug = models.SlugField(_("slug"), unique=True)
    fips = models.PositiveIntegerField(_("FIPS"), max_length=5, blank=True, help_text=_("See <a href=\"http://en.wikipedia.org/wiki/FIPS_county_code\">FIPS County Code</a>."))
    county_seat = models.CharField(_("county seat"), max_length=250, blank=True)
    created = models.PositiveIntegerField(_("year created"), max_length=4, blank=True)
    population = models.PositiveIntegerField(_("population"), max_length=10, blank=True)
    area = models.PositiveIntegerField(_("area"), max_length=6, blank=True, help_text=_("In square miles"))
    google_map = models.CharField(_("google maps ID"), blank=True, max_length=43, help_text=_("Example: 100086641935463435263.00043d849437ec4ec3308"))

    class Meta:
        ordering = ["name"]
        verbose_name = _("district")
        verbose_name_plural = _("districts")

    def __unicode__(self):
        return u"%s" % (self.name)


class Place(models.Model):
    name = models.CharField(_("name"), max_length=250)
    slug = models.SlugField(_("slug"), unique=True)
    address = models.CharField(_("address"), max_length=250, blank=True, help_text=_("Optional, but add them when possible."))
    city = models.CharField(_("city"), max_length=250, blank=True)
    district = models.ForeignKey(District, blank=True, null=True)
    state = models.CharField(_("state"), choices=US_STATES, max_length=255, blank=True)
    zipcode = models.CharField(_("ZIP code"), max_length=11, blank=True)
    country = models.CharField(_("country"), max_length=250, default="USA", blank=True)
    description = models.TextField(_("description"), blank=True, help_text=_("Please use <a href=\"http://en.wikipedia.org/wiki/Markdown\">Markdown styling</a>."))
    photo = models.ImageField(_("photo"), upload_to="places/", blank=True)
    photo_url = models.URLField(_("photo's origin URL"), blank=True, help_text=_("Probably the original Flickr photo page"))
    photographer = models.CharField(_("photographer's name"), max_length=250, blank=True)
    photographer_url = models.URLField(_("photographer's URL"), blank=True, help_text=_("Could be a Flickr profile page, Facebook profile page, etc."))
    latitude = models.DecimalField(_("latitude"), max_digits=9, decimal_places=6, help_text=_("Use <a href=\"http://www.getlatlon.com\">GetLatLon.com</a> to find the latitude. Only six places after the decimal are allowed."))
    longitude = models.DecimalField(_("longitude"), max_digits=9, decimal_places=6, help_text=_("Use <a href=\"http://www.getlatlon.com\">GetLatLon.com</a> to find the longitude. Only six places after the decimal are allowed."))
    street = models.CharField(_("street view"), blank=True, max_length=250, help_text=_("1. Find location on <a href=\"http://maps.google.com\">Google Maps</a><br />2. Click on &ldquo;Street View&rdquo; and adjust camera.<br />3. Click &ldquo;Link to this Page&rdquo; > &ldquo;Customize and preview embedded map&rdquo;<br />4. Scroll to number three and extract quoted URL in src=\"\" from &lt;iframe&gt; HTML tag."))
    url = models.URLField(_("URL"), blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _("place")
        verbose_name_plural = _("places")

    def __unicode__(self):
        return u"%s" % (self.name)

    def get_absolute_url(self):
        return reverse("places_place_detail", args=[str(self.slug)])

    def website(self):
        domain = re.sub(r"(http|https)://(?:www\.)", "", self.url)
        pretty = re.sub(r"\/$", "", domain)
        return u"%s" % (pretty)
