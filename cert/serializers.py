from rest_framework import serializers
from .models import Certificates, cert_choices


class CertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certificates
        fields = ('issuer_common_name', 'issuer_organization', 'message', 'result_color_hex', 'subject_common_name', 'subject_organization', 'validation_result', 'validation_result_short')



