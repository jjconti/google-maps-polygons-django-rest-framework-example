from models import Polygon
from rest_framework import viewsets
from mozio_poly.saver.serializers import PolygonSerializer


class PolygonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows polygons to be listed or added.
    """
    last_date = Polygon.objects.latest('post_date').post_date
    queryset = Polygon.objects.filter(post_date=last_date)

    serializer_class = PolygonSerializer

    def get_queryset(self):
        last_date = Polygon.objects.latest('post_date').post_date
        return Polygon.objects.filter(post_date=last_date) # Retrieve the most recent data