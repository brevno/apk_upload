# Django REST API example

A prototype application providing ability to upload and browse APK files via
Django REST framework.

Usage example:
```rest
GET /api/applications/
[
    {
        "application": "/media/525db2b8-e9c9-46be-8275-b93e285bfecd.apk",
        "package_name": "com.whatsapp",
        "package_vesion_code": "1234"
    },
    ...
]
```

## Installation steps

```
git clone https://github.com/brevno/apk_upload
```
Inside the project's folder:
```
virtualenv env
pip install -r requirements txt
python manage.py migrate
```
### Run tests
```
python manage.py test
```
## Installation using docker-compose


```
git clone https://github.com/brevno/apk_upload
```
Inside the project's folder:
```
docker-compose up
```
