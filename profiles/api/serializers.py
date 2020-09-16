from rest_framework import serializers
from profiles.models import Profile
from homes.api.serializers import HomeSerializer
from homes.api.serializers import SaveHomeSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"
