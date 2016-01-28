from mozio_poly.saver.models import Polygon
from rest_framework import serializers


class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = ('encoded', 'post_date')