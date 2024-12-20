from typing import Any
from django.db import models


class Project(models.Model):
    """
    A class representing a project
    Attributes:
        title (str): project title
        description (text): project description
        technology(str): project stack
    """

    title: models.CharField = models.CharField(max_length=100)
    description: models.TextField = models.TextField()
    technology: models.CharField = models.CharField(max_length=20)
