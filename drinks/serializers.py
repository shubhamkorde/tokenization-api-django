# Describes the structure of python object to JSON
from rest_framework import serializers
from .models import Drink
from .models import Transcription
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']


class TranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcription
        fields = ['id', 'name', 'text', 'tokens']
