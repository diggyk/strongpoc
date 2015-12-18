from django.shortcuts import render
from rest_framework import viewsets, filters
import django_filters


from . import models
from . import serializers


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = models.ServiceProvider.objects.all()
    serializer_class = serializers.ServiceProviderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)


class PointOfContactViewSet(viewsets.ModelViewSet):
    queryset = models.PointOfContact.objects.all()
    serializer_class = serializers.PointOfContactSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('team', 'contact_type', 'service_provider')