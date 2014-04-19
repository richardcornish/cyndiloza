from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model


class About(models.Model):
    user = models.ForeignKey(get_user_model())
    blurb = models.TextField(help_text="Appears on the homepage. Please use <a href=\"http://en.wikipedia.org/wiki/Markdown\">Markdown styling</a> for links.")
    body = models.TextField()
    photo = models.ImageField(upload_to="about/photo/", blank=True)
    resume = models.FileField(upload_to="about/resume/", blank=True, help_text="Please upload a PDF.")

    class Meta:
        ordering = ["user"]

    def __unicode__(self):
        return u"%s" % self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("about_list")
