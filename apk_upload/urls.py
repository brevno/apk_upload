from django.conf.urls import url
from .views import FileView

urlpatterns = [
    url(r'^$', FileView.as_view(), name='files_view')
]
