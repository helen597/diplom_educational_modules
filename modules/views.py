from rest_framework import viewsets
from modules.serializers import ModuleSerializer
from modules.models import Module


# Create your views here.
class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
