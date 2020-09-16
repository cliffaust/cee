from django_filters import rest_framework as filters
from homes.models import Home


class HomeFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="home_price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="home_price", lookup_expr="lte")
    min_year = filters.NumberFilter(field_name="year_built", lookup_expr="gte")
    max_year = filters.NumberFilter(field_name="year_built", lookup_expr="lte")
    min_bedroom_numbers = filters.NumberFilter(
        field_name="number_bedrooms", lookup_expr="gte"
    )
    max_bedroom_numbers = filters.NumberFilter(
        field_name="number_bedrooms", lookup_expr="lte"
    )
    min_bathroom_numbers = filters.NumberFilter(
        field_name="number_bathrooms", lookup_expr="gte"
    )
    max_bathroom_numbers = filters.NumberFilter(
        field_name="number_bathrooms", lookup_expr="lte"
    )
    home_feature = filters.CharFilter(
        field_name="general_home_features__home_feature", lookup_expr="icontains"
    )
    min_home_size = filters.NumberFilter(field_name="home_size", lookup_expr="gte")
    max_home_size = filters.NumberFilter(field_name="home_size", lookup_expr="lte")
    home_type = filters.CharFilter(field_name="home_type", lookup_expr="icontains")

    class Meta:
        model = Home
        fields = [
            "min_price",
            "max_price",
            "home_feature",
            "home_type",
            "min_bedroom_numbers",
            "max_bedroom_numbers",
            "min_bathroom_numbers",
            "max_bathroom_numbers",
            "min_home_size",
            "max_home_size",
            "min_year",
            "max_year",
        ]