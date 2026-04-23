from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60)
    total_footprint = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'total_footprint': self.total_footprint
        }

