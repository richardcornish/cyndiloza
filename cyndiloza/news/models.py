from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from cyndiloza.news import managers
from cyndiloza.places.models import Place
from cyndiloza.people.models import Person


class Author(models.Model):
    name = models.CharField(_("name"), max_length=250)

    class Meta:
        ordering = ["name"]
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __unicode__(self):
        return u"%s" % (self.name)


class Section(models.Model):
    name = models.CharField(_("name"), max_length=250, help_text=_("Name of the section under which the article appeared, e.g. Business, Features, etc."))
    slug = models.SlugField(_("slug"), unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _("section")
        verbose_name_plural = _("sections")

    def __unicode__(self):
        return u"%s" % (self.name)


class Edition(models.Model):
    name = models.CharField(_("name"), max_length=250, help_text=_("Name of the edition under which the article appeared, e.g. Final, Evening, etc."))

    class Meta:
        ordering = ["name"]
        verbose_name = _("edition")
        verbose_name_plural = _("editions")

    def __unicode__(self):
        return u"%s" % (self.name)


class Publication(models.Model):
    FREQUENCY_CHOICES = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Bi-weekly', 'Bi-weekly'),
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Semesterly', 'Semesterly'),
        ('Yearly', 'Yearly'),
    )
    FORMAT_CHOICES = (
        ('Broadsheet', 'Broadsheet'),
        ('Tabloid', 'Tabloid'),
        ('Compact', 'Compact'),
        ('Berliner', 'Berliner'),
        ('Newsletter', 'Newsletter'),
        ('Magazine', 'Magazine'),
        ('Website', 'Website'),
        ('Blog', 'Blog'),
    )
    name = models.CharField(_("name"), max_length=250)
    slug = models.SlugField(_("slug"), unique=True)
    frequency = models.CharField(_("frequency"), max_length=10, choices=FREQUENCY_CHOICES, blank=True)
    format = models.CharField(_("format"), max_length=10, choices=FORMAT_CHOICES, blank=True)
    circulation = models.PositiveIntegerField(_("circulation"), blank=True, null=True)
    place = models.ForeignKey(Place)
    description = models.TextField(_("description"), help_text=_("A few words about the publication. Please use <a href=\"http://en.wikipedia.org/wiki/Markdown\">Markdown styling</a>."))
    url = models.URLField(_("URL"), default="http://", blank=True)
    logo = models.ImageField(_("logo"), upload_to="news/logos/", blank=True, help_text=_("A large, clean version of the logo."))
    icon = models.ImageField(_("icon"), upload_to="places/icons/", blank=True)
    rank = models.PositiveIntegerField(_("rank"), unique=True, help_text=_("The rank of this publication by order of importance, with \"1\" as the most important."))

    objects = managers.VisibilityManager()

    # city = models.CharField(_("city"), max_length=50, blank=True)
    # state = models.CharField(_("state"), choices=US_STATES, max_length=255, blank=True)
    # latitude = models.DecimalField(_("latitude"), max_digits=8, decimal_places=6, blank=True, null=True)
    # longitude = models.DecimalField(_("longitude"), max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        ordering = ["rank", "name"]
        verbose_name = _("publication")
        verbose_name_plural = _("publications")

    def __unicode__(self):
        return u"%s" % (self.name)

    def get_absolute_url(self):
        return reverse("news_publication_detail", args=[str(self.slug)])

    def website(self):
        domain = re.sub(r"http://(?:www\.)", "", self.url)
        pretty = re.sub(r"\/$", "", domain)
        return u"%s" % (pretty)

    def places(self):
        publication_places = []
        for article in self.article_set.all():
            try:
                if article.place != None:
                    if article.place not in publication_places:
                        publication_places.append(article.place)
            except:
                pass
        return publication_places


class Prom(models.Model):
    theme = models.CharField(_("theme"), max_length=250)
    slug = models.SlugField(_("slug"), unique=True)
    school = models.ForeignKey(Place, related_name="school")
    location = models.ForeignKey(Place, related_name="location")
    distance = models.DecimalField(max_digits=2, decimal_places=1, help_text="Distance between locations in miles. Decimals are OK.")
    start_time = models.DateTimeField(_("start time"))
    end_time = models.TimeField(_("end time"))
    color_one = models.CharField(_("color one"), blank=True, max_length=50)
    color_one_hex = models.CharField(_("color one hex"), blank=True, max_length=6)
    color_two = models.CharField(_("color two"), blank=True, max_length=50)
    color_two_hex = models.CharField(_("color two hex"), blank=True, max_length=6)
    color_three = models.CharField(_("color three"), blank=True, max_length=50)
    color_three_hex = models.CharField(_("color three hex"), blank=True, max_length=6)
    notes = models.TextField(_("notes"), blank=True)
    published = models.BooleanField(_("published"), default=True)

    class Meta:
        ordering = ["school"]
        verbose_name = _("prom")
        verbose_name_plural = _("proms")

    def __unicode__(self):
        return u"%s" % (self.theme)


class Article(models.Model):
    MAPTYPE_CHOICES = (
        ('G_NORMAL_MAP', 'Normal'),
        ('G_SATELLITE_MAP', 'Satellite'),
        ('G_HYBRID_MAP', 'Hybrid'),
        ('G_PHYSICAL_MAP', 'Terrain'),
    )
    headline = models.CharField(max_length=250)
    slug = models.SlugField(_("slug"), unique=True)
    date = models.DateField(help_text="Written in YYYY-MM-DD format")
    author = models.ForeignKey(Author, default=1)
    contributors = models.CharField(max_length=250, blank=True, help_text="For contributing authors, separated by commas.")
    publication = models.ForeignKey(Publication, default=4)
    section = models.ForeignKey(Section, blank=True, null=True)
    edition = models.ForeignKey(Edition, blank=True, null=True)
    page = models.CharField(max_length=4, blank=True)
    place = models.ForeignKey(Place, null=True, blank=True, help_text="Select one place that sums up your article, if applicable. A map of the location will appear on the article page.")
    maptype = models.CharField("Map type", max_length=15, blank=True, choices=MAPTYPE_CHOICES)
    summary = models.TextField(blank=True, help_text="Optional, but it looks snappy with anything, even the lead of a story.")
    body = models.TextField(help_text="Did you...<br />1. Change curly marks and apostrophes to <strong>straight</strong> marks and apostrophes?<br />2. Make a <strong>line break</strong> between all paragraphs?<br />3. Use <strong><a href=\"http://en.wikipedia.org/wiki/Markdown\">Markdown styling</a></strong> for headers (####), lists and links?")
    note = models.TextField("Editor's note", blank=True, help_text="For special notes that precede a newspaper article, like those for a series.")
    photo = models.ImageField(upload_to="news/photos/", blank=True, help_text="Did you...<br />1. Download the <strong>enlarged</strong> version of the photo?<br />2. Rename the photo with a meaningful file name?<br />3. Rename the file extension from &ldquo;.jpeg&rdquo; to &ldquo;.jpg&rdquo;?")
    photo_url = models.URLField("Photo URL", blank=True, help_text="Most likely the originating Flickr photo page, but if an &ldquo;official&rdquo; photo, it could be the photo page on the publication's website.")
    caption = models.TextField(blank=True, help_text="Did you replace curly marks with straight marks?")
    photographer = models.CharField(max_length=250, blank=True)
    photographer_url = models.URLField("Photographer's URL", blank=True, help_text="Could be a Flickr profile page, Facebook profile page, etc.")
    sidebarheadline = models.CharField("Sidebar headline", max_length=250, blank=True)
    sidebarcontent = models.TextField("Sidebar story", blank=True, help_text="Use <a href=\"http://en.wikipedia.org/wiki/Markdown\">Markdown</a> as necessary for headers (####), lists and links.")
    document_title = models.CharField(max_length=250, blank=True, help_text="The title of a document related to the article.")
    document = models.FileField(upload_to="news/documents/", blank=True, help_text="A document related to the article.")
    dipity = models.CharField(max_length=255, blank=True, help_text="The &lt;iframe&gt; code for a <a href=\"http://www.dipity.com\">Dipity</a> timeline.")
    people = models.ManyToManyField(Person, blank=True, null=True)
    url = models.URLField("URL", blank=True, help_text="URL of the article on the publication's official website.")
    published = models.BooleanField(default=True, help_text="Check this box if you want the article published live on the website.")
    featured = models.BooleanField(default=False, help_text="Check this box if you want the article prominently featured on the website homepage.")

    objects = managers.VisibilityManager()

    class Meta:
        ordering = ["-date", "headline"]
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __unicode__(self):
        return u"%s" % (self.headline)

    def get_absolute_url(self):
        return reverse("news_article_detail", args=[str(self.slug)])

    def get_previous_published(self):
        return self.get_previous_by_date(published=True)

    def get_next_published(self):
        return self.get_next_by_date(published=True)


class FavoriteList(models.Model):
    title = models.CharField(_("title"), max_length=250)
    slug = models.SlugField(_("slug"), unique=True)
    published = models.BooleanField(_("published"), default=True, help_text="Check this box if you want the list published live on the website.")

    class Meta:
        ordering = ["title"]
        verbose_name = _("favorite list")
        verbose_name_plural = _("favorite lists")

    def __unicode__(self):
        return u"%s" % (self.title)


class Favorite(models.Model):
    rank = models.PositiveIntegerField(_("rank #"))
    article = models.ForeignKey(Article)
    favoritelist = models.ForeignKey(FavoriteList, verbose_name="Favorite list")

    class Meta:
        ordering = ["rank"]
        verbose_name = _("favorite")
        verbose_name_plural = _("favorites")

    def __unicode__(self):
        return u"%s" % (self.rank)
