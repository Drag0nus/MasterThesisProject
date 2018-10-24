from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from cert import views

router = DefaultRouter()
router.register(r'certs', views.CertificateViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]