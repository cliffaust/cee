from django_filters import rest_framework as filters
from lands.models import Land


class LandFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="land_price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="land_price", lookup_expr="lte")
    min_land_size = filters.NumberFilter(field_name="land_size", lookup_expr="gte")
    max_land_size = filters.NumberFilter(field_name="land_size", lookup_expr="lte")

    class Meta:
        model = Land
        fields = [
            "min_price",
            "max_price",
            "min_land_size",
            "max_land_size",
        ]