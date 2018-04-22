from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import APKFile
from .parsers import APKParser
from .serializers import FileSerializer


class FileView(APIView):

    parser_classes = (APKParser, )

    def get(self, *args, **kwargs):
        serializer = FileSerializer(APKFile.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                file_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
