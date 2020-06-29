from rest_framework import serializers

from .models import ServerUtil

class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServerUtil
        fields = ('server_id', 'cpu_utilization','memory_utilization','disk_utilization')