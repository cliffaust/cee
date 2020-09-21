from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from homes.models import (
    ContactNumber,
    GeneralHomeFeatures,
    Home,
    HomeCoordinate,
    HomeImage,
    HomeReview,
    KitchenFeature,
    OpenDateTime,
    RoomFeature,
    SaveHome,
    SittingRoomFeature,
    HomeVideo,
)
from profiles.models import Profile

from .filterset import HomeFilter
from .permissions import IsUserHome, IsUserHomeInstance, IsUserReview
from .serializers import (
    ContactNumberSerializer,
    GeneralHomeFeaturesSerializer,
    HomeCoordinateSerializer,
    HomeImageSerializer,
    HomeReviewSerializer,
    HomeSerializer,
    KitchenFeatureSerializer,
    OpenDateTimeSerializer,
    RoomFeatureSerializer,
    SaveHomeSerializer,
    SittingRoomFeatureSerializer,
    HomeVideoSerializer,
)


class HomeListView(generics.ListAPIView):
    serializer_class = HomeSerializer
    filterset_class = HomeFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = [
        "date_posted",
        "home_price",
        "number_bedrooms",
        "number_bathrooms",
        "home_size",
    ]
    search_fields = ["address", "city"]

    def get_queryset(self):
        queryset = Home.objects.all()

        profile_pk = self.kwargs.get("profile_pk")
        if profile_pk is not None:
            profile = generics.get_object_or_404(Profile, pk=profile_pk)
            queryset = Home.objects.filter(profile=profile)

        return queryset


class HomeCreateView(generics.CreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        profile_pk = self.kwargs.get("profile_pk")
        profile = generics.get_object_or_404(Profile, pk=profile_pk)
        if profile.user != self.request.user:
            raise PermissionDenied("You are not allowed add a home to this profile")
        serializer.save(user=self.request.user, profile=profile)


class HomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HomeSerializer
    permission_classes = [IsUserHomeInstance]
    lookup_field = "slug"

    def get_queryset(self):
        queryset = Home.objects.all()
        slug = self.kwargs.get("slug")

        if slug is not None:
            queryset = Home.objects.filter(slug=slug)
        return queryset


class HomeImageCreateView(generics.CreateAPIView):
    queryset = HomeImage.objects.all()
    serializer_class = HomeImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)
        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        if not home_queryset.exists():
            raise PermissionDenied("You can't add an image to this home")
        return serializer.save(home=home)


class HomeImageListView(generics.ListAPIView):
    serializer_class = HomeImageSerializer

    def get_queryset(self):
        queryset = HomeImage.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = HomeImage.objects.filter(home=home)

        return queryset


class HomeVideoCreateView(generics.CreateAPIView):
    queryset = HomeVideo.objects.all()
    serializer_class = HomeVideoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)
        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        if not home_queryset.exists():
            raise PermissionDenied("You can't add a video to this home")
        return serializer.save(home=home)


class HomeVideoListView(generics.ListAPIView):
    serializer_class = HomeVideoSerializer

    def get_queryset(self):
        queryset = HomeVideo.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = HomeVideo.objects.filter(home=home)

        return queryset


class HomeImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeImage.objects.all()
    serializer_class = HomeImageSerializer
    permission_classes = [IsAuthenticated, IsUserHome]


class OpenDataTimeListView(generics.ListAPIView):
    serializer_class = OpenDateTimeSerializer

    def get_queryset(self):
        queryset = OpenDateTime.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = OpenDateTime.objects.filter(home=home)

        return queryset


class OpenDateTimeCreateView(generics.CreateAPIView):
    queryset = OpenDateTime.objects.all()
    serializer_class = OpenDateTimeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)

        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        if not home_queryset.exists():
            raise PermissionDenied("You can't add a date to this home")
        serializer.save(home=home)


class OpenDateTimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpenDateTime.objects.all()
    serializer_class = OpenDateTimeSerializer
    permission_classes = [IsAuthenticated, IsUserHome]


class ContactNumberListView(generics.ListAPIView):
    serializer_class = ContactNumberSerializer

    def get_queryset(self):
        queryset = ContactNumber.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = ContactNumber.objects.filter(home=home)

        return queryset


class ContactNumberCreateView(generics.CreateAPIView):
    queryset = ContactNumber.objects.all()
    serializer_class = ContactNumberSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)

        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        if not home_queryset.exists():
            raise PermissionDenied("You can't add a number to this home")
        serializer.save(home=home)


class ContactNumberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactNumber.objects.all()
    serializer_class = ContactNumberSerializer
    permission_classes = [IsAuthenticated, IsUserHome]


class HomeCoordinateListView(generics.ListAPIView):
    serializer_class = HomeCoordinateSerializer

    def get_queryset(self):
        queryset = HomeCoordinate.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = HomeCoordinate.objects.filter(home=home)

        return queryset


class HomeCoordinateCreateView(generics.CreateAPIView):
    queryset = HomeCoordinate.objects.all()
    serializer_class = HomeCoordinateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)

        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        home_coordinate_queryset = HomeCoordinate.objects.filter(home=home_pk)

        if not home_queryset.exists():
            raise PermissionDenied("You can't add a coordinate to this home")

        elif home_coordinate_queryset.exists():
            raise PermissionDenied("You can't add more than one coordinate")

        serializer.save(home=home)


class HomeCoordinateDetailView(generics.RetrieveUpdateAPIView):
    queryset = HomeCoordinate.objects.all()
    serializer_class = HomeCoordinateSerializer


class HomeReviewListView(generics.ListAPIView):
    serializer_class = HomeReviewSerializer

    def get_queryset(self):
        queryset = HomeReview.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = HomeReview.objects.filter(home=home)

        return queryset


class HomeReviewCreateView(generics.CreateAPIView):
    queryset = HomeReview.objects.all()
    serializer_class = HomeReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)

        review_queryset = HomeReview.objects.filter(user=self.request.user, home=home)

        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        if review_queryset.exists():
            raise PermissionDenied("User has already reviewed this home")

        elif home_queryset.exists():
            raise PermissionDenied("You can't make a review on your home")

        serializer.save(home=home, user=self.request.user)


class HomeReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeReview.objects.all()
    serializer_class = HomeReviewSerializer
    permission_classes = [IsAuthenticated, IsUserReview]


class RoomFeatureListView(generics.ListAPIView):
    serializer_class = RoomFeatureSerializer

    def get_queryset(self):
        queryset = RoomFeature.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = RoomFeature.objects.filter(home=home)

        return queryset


class RoomFeatureCreateView(generics.CreateAPIView):
    queryset = RoomFeature.objects.all()
    serializer_class = RoomFeatureSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)

        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        if not home_queryset.exists():
            raise PermissionDenied("You can't add a feature to this home")
        serializer.save(home=home)


class GeneralHomeFeaturesListView(generics.ListAPIView):
    serializer_class = GeneralHomeFeaturesSerializer

    def get_queryset(self):
        queryset = GeneralHomeFeatures.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = GeneralHomeFeatures.objects.filter(home=home)

        return queryset


class GeneralHomeFeaturesCreateView(generics.CreateAPIView):
    queryset = GeneralHomeFeatures.objects.all()
    serializer_class = GeneralHomeFeaturesSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)

        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        if not home_queryset.exists():
            raise PermissionDenied("You can't add a feature to this home")

        elif home.general_home_features.filter(
            home_feature=self.request.data["home_feature"].lower()
        ).exists():
            raise PermissionDenied("You can't add the same feature twice")
        serializer.save(home=home)


class KitchenFeatureListView(generics.ListAPIView):
    serializer_class = KitchenFeatureSerializer

    def get_queryset(self):
        queryset = KitchenFeature.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = KitchenFeature.objects.filter(home=home)

        return queryset


class KitchenFeatureCreateView(generics.CreateAPIView):
    queryset = KitchenFeature.objects.all()
    serializer_class = KitchenFeatureSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)

        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        if not home_queryset.exists():
            raise PermissionDenied("You can't add a feature")
        serializer.save(home=home)


class SittingRoomFeatureListView(generics.ListAPIView):
    serializer_class = SittingRoomFeatureSerializer

    def get_queryset(self):
        queryset = SittingRoomFeature.objects.all()

        home_pk = self.kwargs.get("home_pk")
        if home_pk is not None:
            home = generics.get_object_or_404(Home, pk=home_pk)
            queryset = SittingRoomFeature.objects.filter(home=home)

        return queryset


class SittingRoomFeatureCreateView(generics.CreateAPIView):
    queryset = SittingRoomFeature.objects.all()
    serializer_class = SittingRoomFeatureSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)

        home_queryset = Home.objects.filter(id=home_pk, user=self.request.user)

        if not home_queryset.exists():
            raise PermissionDenied("You can't add a feature")
        serializer.save(home=home)


class SaveHomeCreateView(generics.CreateAPIView):
    queryset = SaveHome.objects.all()
    serializer_class = SaveHomeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        home_pk = self.kwargs.get("home_pk")
        profile_pk = self.kwargs.get("profile_pk")
        home = generics.get_object_or_404(Home, pk=home_pk)
        profile = generics.get_object_or_404(Profile, pk=profile_pk)

        if profile.user != self.request.user:
            raise PermissionDenied("You are not allowed to save this home")
        elif profile.saved_homes.filter(home=home).exists():
            raise PermissionDenied("You have already saved this home")
        elif home.user == profile.user:
            raise PermissionDenied("You are not allowed to save your home")
        serializer.save(home=home, profile=profile, user=self.request.user)


class SaveHomeListView(generics.ListAPIView):
    serializer_class = SaveHomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SaveHome.objects.filter(user=self.request.user)


class SaveHomeDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = SaveHomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SaveHome.objects.filter(user=self.request.user)


class SaveHomeAPIView(APIView):
    serializer_class = HomeSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        home = generics.get_object_or_404(Home, pk=pk)
        user = request.user

        home.saves.remove(user)
        home.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(home, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        home = generics.get_object_or_404(Home, pk=pk)
        user = request.user

        home.saves.add(user)
        home.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(home, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
