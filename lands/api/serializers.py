from rest_framework import serializers
from lands.models import (
    Land,
    LandCoordinate,
    LandImage,
    LandVideo,
    LandReview,
    OpenDateTime,
    ContactNumber,
    SaveLand,
)
from django.forms.models import model_to_dict


class LandCoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandCoordinate
        exclude = ["land"]


class ContactNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactNumber
        exclude = ["land"]


class OpenDateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenDateTime
        exclude = ["land"]


class LandReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LandReview
        exclude = ["land"]


class LandImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandImage
        exclude = ["land"]


class LandVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandVideo
        exclude = ["land"]


class SaveLandSerializer(serializers.ModelSerializer):
    saved_land = serializers.SerializerMethodField()

    class Meta:
        model = SaveLand
        exclude = ["land", "profile", "user"]

    def get_saved_land(self, instance):
        data = model_to_dict(instance.land)
        return {
            "land_id": data["id"],
        }


class LandSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    save_count = serializers.SerializerMethodField()
    has_user_saved = serializers.SerializerMethodField()
    date_posted = serializers.StringRelatedField(read_only=True)
    slug = serializers.StringRelatedField(read_only=True)
    user_email = serializers.SerializerMethodField()

    class Meta:
        model = Land
        exclude = ["profile", "saves"]

    def get_save_count(self, instance):
        return instance.saves.count()

    def get_has_user_saved(self, instance):
        request = self.context.get("request")
        return instance.saves.filter(pk=request.user.pk).exists()

    def get_user_email(self, instance):
        return instance.user.email