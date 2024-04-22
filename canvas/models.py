from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Canvas(models.Model):
    name = models.CharField(max_length=255)
    layers = models.JSONField(default=list)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='canvases')

    def __str__(self):
        return self.name

class Lobby(models.Model):
    canvas = models.OneToOneField(Canvas, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='lobbies')
    roles = models.JSONField(default=dict)

    def add_user(self, user, role):
        """
        Add a user to the lobby with the specified role.
        """
        self.users.add(user)
        self.roles[user.id] = role
        self.save()

    def change_role(self, user, new_role):
        """
        Change the role of an existing user in the lobby.
        """
        if user.id in self.roles:
            self.roles[user.id] = new_role
            self.save()