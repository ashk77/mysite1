from django.db import models

# Create your models here.
class ServerUtil(models.Model):
    server_id = models.CharField(max_length=60)
    cpu_utilization = models.FloatField()
    memory_utilization = models.FloatField()
    disk_utilization = models.FloatField()
    def __str__(self):
        return self.server_id