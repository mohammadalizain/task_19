from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    restaurant_link = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'opening_time',
            'closing_time',
            'restaurant_link'
            ]


class RestaurantDetailSerializer(serializers.ModelSerializer):
    restaurant_link2 = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'opening_time',
            'closing_time',
            'restaurant_link2',
            ]

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    restaurant_link3 = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'opening_time',
            'closing_time',
            'restaurant_link3',
            ]