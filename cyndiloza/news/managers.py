from django.db import models
from django.utils import timezone
from django.db.models import Q


class VisibilityManager(models.Manager):
    def published(self):
        return self.get_query_set().filter(published=True)
