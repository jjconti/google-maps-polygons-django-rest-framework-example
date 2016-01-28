from django.conf.urls import url, include
from rest_framework import routers
from mozio_poly.saver import views

# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()
router.register(r'polygons', views.PolygonViewSet)

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]