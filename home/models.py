# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customers(models.Model):

    #__Customers_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    document = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Customers_FIELDS__END

    class Meta:
        verbose_name        = _("Customers")
        verbose_name_plural = _("Customers")


class Areas(models.Model):

    #__Areas_FIELDS__
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Areas_FIELDS__END

    class Meta:
        verbose_name        = _("Areas")
        verbose_name_plural = _("Areas")


class Analysis(models.Model):

    #__Analysis_FIELDS__
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    data_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    description = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Analysis_FIELDS__END

    class Meta:
        verbose_name        = _("Analysis")
        verbose_name_plural = _("Analysis")


class Files(models.Model):

    #__Files_FIELDS__
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    file = models.CharField(max_length=255, null=True, blank=True)

    #__Files_FIELDS__END

    class Meta:
        verbose_name        = _("Files")
        verbose_name_plural = _("Files")



#__MODELS__END
