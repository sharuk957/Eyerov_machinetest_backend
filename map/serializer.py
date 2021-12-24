from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Imagedata

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Imagedata
        fields = '__all__'