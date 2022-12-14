from rest_framework import serializers
from .models import MChild


class MChileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MChild
        fields=['name','gender','age','ageNow',
                'alldressing','occrAdd','occrDate',
                'writngTarget','inform']