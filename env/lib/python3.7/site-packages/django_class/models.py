# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import public
import pydoc
import sys

APP_LABEL = 'django_class'


def validate_module_name(module_name):
    if module_name == "__main__":
        raise ValidationError("'__main__' module_name not allowed")


@public.add
class AbsClass(models.Model):
    """abstract class model. fields: `module_name`, `class_name`. methods: `getmodule()`, `getclass()`"""

    class Meta:
        abstract = True
        app_label = APP_LABEL
        ordering = ['module_name', 'class_name']
        unique_together = ('module_name', 'class_name',)

    module_name = models.CharField(_('Python module'), max_length=255, null=True, blank=True, editable=False, validators=[validate_module_name])
    class_name = models.CharField(_('Python class'), max_length=255, null=True, blank=True, editable=False)

    def getmodule(self):
        if self.module_name:
            if self.module_name in sys.modules:
                return sys.modules[self.module_name]
            return pydoc.locate(self.module_name)

    def getclass(self):
        if self.module_name and self.class_name:
            fullname = "%s.%s" % (self.module_name, self.class_name)
            return pydoc.locate(fullname)

    def clean_fields(self):
        if self.module_name == "__main__":
            raise ValidationError("'__main__' module_name not allowed")

    def save(self, *args, **kwargs):
        self.clean_fields()
        models.Model.save(self, *args, **kwargs)

    def __str__(self):
        string = '<Class id={id} module_name="{module_name}" class_name="{class_name}">'
        return string.format(
            id=self.id,
            module_name=self.module_name,
            class_name=self.class_name,
        )

    def __repr__(self):
        return self.__str__()


@public.add
class Class(AbsClass):
    """Class model. fields: `module_name`, `class_name`. methods: `getmodule()`, `getclass()`"""

    class Meta:
        app_label = APP_LABEL
        ordering = ['module_name', 'class_name']
        unique_together = ('module_name', 'class_name',)
