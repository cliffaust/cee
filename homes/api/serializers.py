from rest_framework import serializers
from homes.models import (
    Home,
    HomeImage,
    HomeCoordinate,
    OpenDateTime,
    ContactNumber,
    HomeReview,
    RoomFeature,
    KitchenFeature,
    SittingRoomFeature,
    SaveHome,
    GeneralHomeFeatures,
    HomeVideo,
)

from django.forms.models import model_to_dict


class HomeCoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCoordinate
        exclude = ["home"]


class ContactNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNumber
        exclude = ["home"]


class OpenDateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenDateTime
        exclude = ["home"]


class HomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeImage
        exclude = ["home"]


class HomeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeVideo
        exclude = ["home"]


class HomeReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HomeReview
        exclude = ["home"]


class RoomFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFeature
        exclude = ["home"]


class KitchenFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitchenFeature
        exclude = ["home"]


class SittingRoomFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SittingRoomFeature
        exclude = ["home"]


class GeneralHomeFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralHomeFeatures
        exclude = ["home"]


class SaveHomeSerializer(serializers.ModelSerializer):
    saved_home = serializers.SerializerMethodField()

    class Meta:
        model = SaveHome
        exclude = ["home", "profile", "user"]

    def get_saved_home(self, instance):
        data = model_to_dict(instance.home)
        return {
            "home_id": data["id"],
        }


class HomeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    save_count = serializers.SerializerMethodField()
    has_user_saved = serializers.SerializerMethodField()
    date_posted = serializers.StringRelatedField(read_only=True)
    slug = serializers.StringRelatedField(read_only=True)
    user_email = serializers.SerializerMethodField()

    class Meta:
        model = Home
        exclude = ["profile", "saves"]

    def get_save_count(self, instance):
        return instance.saves.count()

    def get_has_user_saved(self, instance):
        request = self.context.get("request")
        return instance.saves.filter(pk=request.user.pk).exists()

    def get_user_email(self, instance):
        return instance.user.email
