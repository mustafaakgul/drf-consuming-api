from django.db import models


class InfuraInitial(models.Model):
    result = models.CharField(max_length=200)
    #body_id = models.CharField(max_length=100)
    jsonrpc = models.CharField(max_length=100)

    def __str__(self):
        return self.result