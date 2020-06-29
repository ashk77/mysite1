from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServerSerializer
from .models import ServerUtil


class ServerViewSet(viewsets.ModelViewSet):
    queryset = ServerUtil.objects.all().order_by('server_id')
    serializer_class = ServerSerializer