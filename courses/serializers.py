from rest_framework import serializers
from .models import Lectures

class LecturesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Lectures
        fields = ['title','sections']