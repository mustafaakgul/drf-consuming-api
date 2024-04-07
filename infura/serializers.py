from rest_framework import serializers
from .models import *


class InfuraInitialSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfuraInitial
        fields = '__all__'