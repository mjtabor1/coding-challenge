from django.db import models


class Referral(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PageView(models.Model):
    hits = models.PositiveIntegerField(default=0)


