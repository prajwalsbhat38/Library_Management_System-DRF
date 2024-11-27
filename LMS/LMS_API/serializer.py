from .models import Books
from rest_framework import serializers

class Books_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'