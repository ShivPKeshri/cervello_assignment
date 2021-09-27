from django.urls import path, include
from .views import upload_excel, LecturesList, LecturesDetail

urlpatterns = [
    # path('excel/', upload_excel),
    path('lecture/', LecturesList.as_view()),
    path('lecture/<int:id>/', LecturesDetail.as_view()),
]