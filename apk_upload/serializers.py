from rest_framework import serializers
from .models import APKFile


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = APKFile
        fields = ('file', 'package_name', 'package_version_code')
