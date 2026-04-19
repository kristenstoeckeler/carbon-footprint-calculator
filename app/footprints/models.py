from django.db import models


class Lifestyle(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Choice(models.Model):
    name = models.CharField(max_length=60, unique=True)
    carbon = models.IntegerField()
    lifestyle = models.ForeignKey(Lifestyle, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserChoice(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'choice')

    def __str__(self):
        return f"{self.user.name} - {self.choice.name}"
