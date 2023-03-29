from django.db import models


class ProfileUSer(models.Model):

    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    bio=models.TextField()
    email=models.EmailField()

    def __str__(self):

        return f"{self.name}-{self.family}"