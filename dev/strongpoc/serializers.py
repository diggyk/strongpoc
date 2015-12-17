from rest_framework import serializers
from . import models


class TeamSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return obj.to_dict()

    class Meta:
        model = models.Team


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceProvider


class ContactTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactType


class PointOfContactSerializer(serializers.ModelSerializer):
    # team = serializers.StringRelatedField()
    team = TeamSerializer()
    # service_provider = ServiceProviderSerializer()
    # contact_type = ContactTypeSerializer()

    def to_representation(self, obj):
        params = self.context['request'].query_params
        expand = params.get('expand')

        return obj.to_dict(expand=expand)

    class Meta:
        model = models.PointOfContact
