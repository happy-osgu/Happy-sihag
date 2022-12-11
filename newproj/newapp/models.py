from django.db import models


class Service(models.Model):
    service_icon = models.CharField(max_length=25)
    service_title = models.CharField(max_length=25)
    service_des = models.TextField()

    def __str__(self):
        return self.service_icon
