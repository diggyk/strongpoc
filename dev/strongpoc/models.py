from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
        }


class ServiceProvider(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class ContactType(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class PointOfContact(models.Model):
    value = models.CharField(max_length=256)
    team = models.ForeignKey(Team, related_name="pocs")
    service_provider = models.ForeignKey(ServiceProvider, related_name="pocs")
    contact_type = models.ForeignKey(ContactType, related_name="pocs")

    def __unicode__(self):
        return "Contact {} for {} {} at {}".format(
            self.team, self.service_provider, self.contact_type, self.value
        )

    def to_dict(self, expand=None):
        if isinstance(expand, basestring):
            expand = [expand]
        if expand is None:
            expand = []

        if "pocs" in expand:
            expand.remove("pocs")

        out = {
            "team": self.team_id if "teams" not in expand else self.team.to_dict(),
            "service_provider": self.service_provider_id,
            "contact_type": self.contact_type_id,
            "value": self.value,
            "id": self.id
        }

        return out

    class Meta:
        unique_together = ("team", "service_provider", "contact_type")
