from django.db import models

# Create your models here.

    # def __str__(self):
    #     return self.name


class Developer(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
         return self.name

class Game(models.Model):
    title=models.CharField(max_length=50)
    developer=models.ForeignKey(Developer , on_delete=models.CASCADE)

