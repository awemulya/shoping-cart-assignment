from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from inventory.viewsets import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )