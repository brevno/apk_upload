from django.db import models


class APKFile(models.Model):
    file = models.FileField(blank=False, null=False)
    package_name = models.CharField(max_length=200, blank=True)
    package_version_code = models.CharField(max_length=20, blank=True)
