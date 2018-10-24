from rest_framework import viewsets
from .models import Certificates
from .serializers import CertificateSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificateSerializer

