from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Courses, Sections, Lectures
from .serializers import LecturesSerializers
from .utils import upload_excel_util

@api_view(['POST'])
def upload_excel(request):
    try:
        file_path = settings.MEDIA_PATH / 'Interview_data_sheet.xlsx'
        print('file_path', file_path)
        upload_excel_util(file_path)    
        data = {'message':'File data uploaded succesfully', 'status':201}
        return Response(data)
    except FileNotFoundError:
        return Response({'message':'File does not exist', 'status':400})
    except Exception as e:
        return Response({'message':'Raised exception','error':str(e), 'status':403})


class LecturesList(generics.ListCreateAPIView):
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializers

class LecturesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lectures.objects.all()
    serializer_class = LecturesSerializers
    lookup_field = 'id'