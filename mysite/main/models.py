from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.text