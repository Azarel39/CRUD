from django.contrib.auth.models import User
from rest_framework import serializers

from crud.models import Person


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
        )
