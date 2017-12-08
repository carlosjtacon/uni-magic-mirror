from models import File
from rest_framework.serializers import ModelSerializer

class FileSerializer(ModelSerializer):
    class Meta:
        model = File
