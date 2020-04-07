from rest_framework import viewsets, permissions
from .models import Lead
from .serializer import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    permission_class = [
        permissions.AllowAny
    ]