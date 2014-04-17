from django.db import models


class VisibilityManager(models.Manager):
    def published(self):
        return self.get_query_set().filter(published=True)
