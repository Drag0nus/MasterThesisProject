from rest_framework import serializers
from .models import FeedbackData


class FeedbackDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeedbackData
        fields = ('firstName', 'lastName', 'webPage', 'subject')
