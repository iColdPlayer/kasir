from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app
# to ensure celery keep start everytime django started
__all__ = ('celery_app')