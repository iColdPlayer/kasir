from __future__ import absolute_import, unicode_literals
from django.db import models
from django.utils import timezone
# Create your models here.
class Stock(models.Model):

    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
