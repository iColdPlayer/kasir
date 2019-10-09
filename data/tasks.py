from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Stock

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def count_stock():
    return Stock.objects.count()