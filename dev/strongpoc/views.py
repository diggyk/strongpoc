from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = models.ServiceProvider.objects.all()
    serializer_class = serializers.ServiceProviderSerializer


class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer


class PointOfContactViewSet(viewsets.ModelViewSet):
    queryset = models.PointOfContact.objects.all()
    serializer_class = serializers.PointOfContactSerializer