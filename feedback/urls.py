from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from feedback import views

router = DefaultRouter()
router.register(r'feedback', views.FedbackDataViewSet)

urlpatterns = [
    url('r^', include(router.urls))

]
