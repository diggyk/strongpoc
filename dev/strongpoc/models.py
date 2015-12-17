from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    def prep_expands(self, expand, self_name):
        if isinstance(expand, basestring):
            expand = [expand]
        if expand is None:
            expand = []

        if self_name in expand:
            expand.remove(self_name)

        return expand

    class Meta:
        abstract = True


class Team(BaseModel):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def to_dict(self, expand=None):
        expand = self.prep_expands(expand, "teams")
        out = {
            "id": self.id,
            "name": self.name,
        }

        return out


class ServiceProvider(BaseModel):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def to_dict(self, expand=None):
        expand = self.prep_expands(expand, "service_providers")
        out = {
            "id": self.id,
            "name": self.name,
        }

        return out


class ContactType(BaseModel):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

    def to_dict(self, expand=None):
        expand = self.prep_expands(expand, "contact_types")
        out = {
            "id": self.id,
            "name": self.name,
        }

        return out


class PointOfContact(BaseModel):
    value = models.CharField(max_length=256)
    team = models.ForeignKey(Team, related_name="pocs")
    service_provider = models.ForeignKey(ServiceProvider, related_name="pocs")
    contact_type = models.ForeignKey(ContactType, related_name="pocs")

    def __unicode__(self):
        return "Contact {} for {} {} at {}".format(
            self.team, self.service_provider, self.contact_type, self.value
        )

    def to_dict(self, expand=None):
        expand = self.prep_expands(expand, "pocs")

        if "all" in expand:
            expand.remove("all")
            expand.extend(["teams", "service_providers", "contact_types"])
        
        out = {
            "id": self.id,
            "value": self.value,
            "team": (
                self.team_id if "teams" not in expand
                else self.team.to_dict(expand)
            ),
            "service_provider": (
                self.service_provider_id if "service_providers" not in expand
                else self.service_provider.to_dict(expand)
            ),
            "contact_type":  (
                self.contact_type_id if "contact_types" not in expand
                else self.contact_type.to_dict(expand)
            )
        }

        return out

    class Meta:
        unique_together = ("team", "service_provider", "contact_type")

