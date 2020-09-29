from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.validators import ValidationError

from lands.models import (
    ContactNumber,
    Land,
    LandCoordinate,
    LandImage,
    LandReview,
    OpenDateTime,
    SaveLand,
    LandVideo,
)
from profiles.models import Profile

from .serializers import (
    ContactNumberSerializer,
    LandCoordinateSerializer,
    LandImageSerializer,
    LandReviewSerializer,
    LandSerializer,
    OpenDateTimeSerializer,
    SaveLandSerializer,
    LandVideoSerializer,
)

from .permissions import IsUserLand, IsUserLandInstance, IsUserReview
from .filterset import LandFilter


class LandListView(generics.ListAPIView):
    serializer_class = LandSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LandFilter
    ordering_fields = [
        "date_posted",
        "land_price",
        "land_size",
    ]
    search_fields = ["address", "city"]

    def get_queryset(self):
        queryset = Land.objects.all()

        profile_pk = self.kwargs.get("profile_pk")
        if profile_pk is not None:
            profile = generics.get_object_or_404(Profile, pk=profile_pk)
            queryset = Land.objects.filter(profile=profile)

        return queryset


class LandCreateView(generics.CreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        profile_pk = self.kwargs.get("profile_pk")
        profile = generics.get_object_or_404(Profile, pk=profile_pk)
        if profile.user != self.request.user:
            raise PermissionDenied("You are not allowed to add a land to this profile")
        serializer.save(user=self.request.user, profile=profile)


class LandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandSerializer
    lookup_field = "slug"
    permission_classes = [IsUserLandInstance]

    def get_queryset(self):
        queryset = Land.objects.all()
        slug = self.kwargs.get("slug")

        if slug is not None:
            queryset = Land.objects.filter(slug=slug)
        return queryset


class LandImageCreateView(generics.CreateAPIView):
    queryset = LandImage.objects.all()
    serializer_class = LandImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        land_pk = self.kwargs.get("land_pk")
        land = generics.get_object_or_404(Land, pk=land_pk)
        land_queryset = Land.objects.filter(id=land_pk, user=self.request.user)

        if not land_queryset.exists():
            raise PermissionDenied("You can't add an image to this land")
        return serializer.save(land=land)


class LandImageListView(generics.ListAPIView):
    serializer_class = LandImageSerializer

    def get_queryset(self):
        queryset = LandImage.objects.all()

        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = LandImage.objects.filter(land=land)

        return queryset


class LandVideoCreateView(generics.CreateAPIView):
    queryset = LandVideo.objects.all()
    serializer_class = LandVideoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        land_pk = self.kwargs.get("land_pk")
        land = generics.get_object_or_404(Land, pk=land_pk)
        land_queryset = Land.objects.filter(id=land_pk, user=self.request.user)

        if not land_queryset.exists():
            raise PermissionDenied("You can't add a video to this land")
        return serializer.save(land=land)


class LandVideoListView(generics.ListAPIView):
    serializer_class = LandVideoSerializer

    def get_queryset(self):
        queryset = LandVideo.objects.all()

        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = LandVideo.objects.filter(land=land)

        return queryset


class LandImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandImageSerializer
    permission_classes = [IsUserLand]

    def get_queryset(self):
        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = LandImage.objects.filter(land=land)

        return queryset


class OpenDataTimeListView(generics.ListAPIView):
    serializer_class = OpenDateTimeSerializer

    def get_queryset(self):
        queryset = OpenDateTime.objects.all()

        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = OpenDateTime.objects.filter(land=land)

        return queryset


class OpenDateTimeCreateView(generics.CreateAPIView):
    queryset = OpenDateTime.objects.all()
    serializer_class = OpenDateTimeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        land_pk = self.kwargs.get("land_pk")
        land = generics.get_object_or_404(Land, pk=land_pk)

        land_queryset = Land.objects.filter(id=land_pk, user=self.request.user)

        if not land_queryset.exists():
            raise PermissionDenied("You can't add a date to this land")
        serializer.save(land=land)


class OpenDateTimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OpenDateTimeSerializer
    permission_classes = [IsUserLand]

    def get_queryset(self):
        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = OpenDateTime.objects.filter(land=land)

        return queryset


class ContactNumberListView(generics.ListAPIView):
    serializer_class = ContactNumberSerializer

    def get_queryset(self):
        queryset = ContactNumber.objects.all()

        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = ContactNumber.objects.filter(land=land)

        return queryset


class ContactNumberCreateView(generics.CreateAPIView):
    queryset = ContactNumber.objects.all()
    serializer_class = ContactNumberSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        land_pk = self.kwargs.get("land_pk")
        land = generics.get_object_or_404(Land, pk=land_pk)

        land_queryset = Land.objects.filter(id=land_pk, user=self.request.user)

        if not land_queryset.exists():
            raise PermissionDenied("You can't add a number to this land")
        serializer.save(land=land)


class ContactNumberDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactNumberSerializer
    permission_classes = [IsUserLand]

    def get_queryset(self):
        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = ContactNumber.objects.filter(land=land)

        return queryset


class LandCoordinateListView(generics.ListAPIView):
    serializer_class = LandCoordinateSerializer

    def get_queryset(self):
        queryset = LandCoordinate.objects.all()

        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = LandCoordinate.objects.filter(land=land)

        return queryset


class LandCoordinateCreateView(generics.CreateAPIView):
    queryset = LandCoordinate.objects.all()
    serializer_class = LandCoordinateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        land_pk = self.kwargs.get("land_pk")
        land = generics.get_object_or_404(Land, pk=land_pk)

        land_queryset = Land.objects.filter(id=land_pk, user=self.request.user)

        land_coordinate_queryset = LandCoordinate.objects.filter(land=land_pk)

        if not land_queryset.exists():
            raise PermissionDenied("You can't add a coordinate to this land")

        elif land_coordinate_queryset.exists():
            raise ValidationError("You can't add more than one coordinate")

        serializer.save(land=land)


class LandCoordinateDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = LandCoordinateSerializer
    permission_classes = [IsUserLand]

    def get_queryset(self):
        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = LandCoordinate.objects.filter(land=land)

        return queryset


class LandReviewListView(generics.ListAPIView):
    serializer_class = LandReviewSerializer

    def get_queryset(self):
        queryset = LandReview.objects.all()

        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = LandReview.objects.filter(land=land)

        return queryset


class LandReviewCreateView(generics.CreateAPIView):
    queryset = LandReview.objects.all()
    serializer_class = LandReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        land_pk = self.kwargs.get("land_pk")
        land = generics.get_object_or_404(Land, pk=land_pk)

        review_queryset = LandReview.objects.filter(user=self.request.user, land=land)

        land_queryset = Land.objects.filter(id=land_pk, user=self.request.user)

        if review_queryset.exists():
            raise ValidationError("User has already reviewed this land")

        elif land_queryset.exists():
            raise PermissionDenied("You can't make a review on your land")

        serializer.save(land=land, user=self.request.user)


class LandReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandReviewSerializer
    permission_classes = [IsUserReview]

    def get_queryset(self):
        land_pk = self.kwargs.get("land_pk")
        if land_pk is not None:
            land = generics.get_object_or_404(Land, pk=land_pk)
            queryset = LandReview.objects.filter(land=land)

        return queryset


class SaveLandCreateView(generics.CreateAPIView):
    queryset = SaveLand.objects.all()
    serializer_class = SaveLandSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        land_pk = self.kwargs.get("land_pk")
        profile_pk = self.kwargs.get("profile_pk")
        land = generics.get_object_or_404(Land, pk=land_pk)
        profile = generics.get_object_or_404(Profile, pk=profile_pk)

        if profile.user != self.request.user:
            raise PermissionDenied("You are not allowed to save this land")
        elif profile.saved_lands.filter(land=land).exists():
            raise ValidationError("You have already saved this land")
        elif land.user == profile.user:
            raise PermissionDenied("You are not allowed to save your land")
        serializer.save(land=land, profile=profile, user=self.request.user)


class SaveLandListView(generics.ListAPIView):
    serializer_class = SaveLandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SaveLand.objects.filter(user=self.request.user)


class SaveLandDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = SaveLandSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SaveLand.objects.filter(user=self.request.user)


class SaveLandAPIView(APIView):
    serializer_class = LandSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        land = generics.get_object_or_404(Land, pk=pk)
        user = request.user

        if land.user == request.user:
            raise PermissionDenied()

        land.saves.remove(user)
        land.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(land, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        land = generics.get_object_or_404(Land, pk=pk)
        user = request.user

        if land.user == request.user:
            raise PermissionDenied("You can't save your land")

        land.saves.add(user)
        land.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(land, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
