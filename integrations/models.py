from django.db import models

# Create your models here.


class WoocommerceStore(models.Model):

    url = models.URLField()
    consumer_key = models.CharField(max_length=128)
    secret_key = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.url