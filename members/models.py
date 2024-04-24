from django.db import models
from django.utils import timezone


class Person(models.Model):
    """Person properties, Used by class Group"""
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128)
    rank = models.CharField(max_length=128)
    joined = models.DateField(null=True, blank=True)
    resigned = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        if self.nickname:
            return f"{self.firstname} \"{self.nickname}\" {self.lastname}"
        else:
            return f"{self.firstname} {self.lastname}"

    class Meta:
            verbose_name_plural = "Military Personnel"

class Group(models.Model):
    """Group for person, Used by class Membership"""
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    """Membership for person"""
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(null=True, blank=True)
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.person.full_name} - {self.group.name}"