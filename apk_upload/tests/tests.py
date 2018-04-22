from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse


client = Client()


class APKUploadTest(TestCase):

    def test_get_all_packages(self):
        response = client.get(reverse('files_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_upload(self):
        with open('apk_upload/tests/Dice.apk', 'rb') as f:
            payload = SimpleUploadedFile('Dice.apk', f.read())
        response = client.post(reverse('files_view'), {'file': payload})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = client.get(reverse('files_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)
        package_version_code = response.data[0].get('package_version_code') \
            if response.data \
            else None
        self.assertEquals(package_version_code, '1')

    def test_upload_bad_file(self):
        payload = SimpleUploadedFile('Application.apk', b'Some rubbish')
        response = client.post(reverse('files_view'), {'file': payload})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = client.get(reverse('files_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 0)
