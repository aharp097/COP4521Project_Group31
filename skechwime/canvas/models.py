from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Canvas(models.Model):
    name = models.CharField(max_length=255)
    layers = models.JSONField(default=list)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='canvases')
    lobby = models.OneToOneField('Lobby', on_delete=models.CASCADE, related_name='uniquecanvas', null=True, blank=True)
    def __str__(self):
        return self.name

class Lobby(models.Model):
    canvas = models.OneToOneField(Canvas, on_delete=models.CASCADE, related_name='uniquelobby', null=True, blank=True, default='')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default='')
    name = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User, related_name='lobbies')
    roles = models.JSONField(default=dict)

    def add_user(self, user, role):
        self.users.add(user)
        self.roles[str(user.id)] = role
        self.save()

    def change_role(self, user, new_role):
        if user.id in self.roles:
            self.roles[str(user.id)] = new_role
            self.save()

    def get_user_role(self, user_id):
        return self.roles.get(str(user_id))