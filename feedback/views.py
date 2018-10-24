from rest_framework import viewsets
from .models import FeedbackData
from .serializers import FeedbackDataSerializer
# Create your views here.

class FedbackDataViewSet(viewsets.ModelViewSet):
    queryset = FeedbackData.objects.all()
    serializer_class = FeedbackDataSerializer
