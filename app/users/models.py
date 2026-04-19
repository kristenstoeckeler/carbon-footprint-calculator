from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

