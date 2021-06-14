from rest_framework import serializers
from .models import PhoneModelClass


class PhoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneModelClass
        fields = '__all__'
