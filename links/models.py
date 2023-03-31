# SHORTLY by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

from django.db import models

class Link(models.Model):
    """
    We make a model to store links.
    """
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)