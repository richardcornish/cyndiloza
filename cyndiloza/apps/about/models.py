from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class About(models.Model):
    user = models.ForeignKey(User)
    blurb = models.TextField(_("blurb"), help_text="Appears on the homepage. Please use <a href=\"http://en.wikipedia.org/wiki/Markdown\">Markdown styling</a> for links.")
    body = models.TextField(_("body"), help_text="About yourself. Appears on the About page. Please use <a href=\"http://en.wikipedia.org/wiki/Markdown\">Markdown styling</a> for links and headings.")
    photo = models.ImageField(_("photo"), upload_to="about/photo/", blank=True, help_text="A photo of yourself.")
    resume = models.FileField(_("resume"), upload_to="about/resume/", blank=True, help_text="Please upload PDFs.")

    class Meta:
        ordering = ["user"]
        verbose_name = _("about")
        verbose_name_plural = _("about")

    def __unicode__(self):
        return u"%s %s" % (self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return reverse("about_about_detail", args=[str(self.id)])
