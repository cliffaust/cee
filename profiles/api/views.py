from rest_framework import generics
from profiles.models import Profile
from .serializers import ProfileSerializer
from .permissions import IsUserProfile
from rest_framework.permissions import IsAuthenticated


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserProfileView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user

        return Profile.objects.filter(user=user)


class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsUserProfile]

    def get_queryset(self):
        user = self.request.user

        return Profile.objects.filter(user=user)
