from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from crud.models import Person
from crudApi.model_serializer import UserModelSerializer, PersonModelSerializer
from crudApi.serializer import UserLoginSerializer, UserSignUpSerializer


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserModelSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class PersonViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Person.objects.filter(is_active=True)
    serializer_class = PersonModelSerializer()

    @action(detail=False, methods=['get'])
    def get_persons(self, request):
        data = {
            'persons': PersonModelSerializer(self.queryset, many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)
