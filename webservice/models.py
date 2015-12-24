from django.db import models


class Boardgames(models.Model):
    name = models.CharField(max_length=150)
    sub_name = models.CharField(max_length=150, null=True)
    date_buy = models.DateTimeField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    description = models.TextField(null=True)
    max_player = models.IntegerField()
    min_player = models.IntegerField()
    image = models.TextField(null=True)
    active = models.BooleanField(default=True)

    extension = models.ForeignKey('self', null=True)

