from .views import (
    ContactNumberCreateView,
    ContactNumberDetailView,
    ContactNumberListView,
    LandCoordinateCreateView,
    LandCoordinateDetailView,
    LandCoordinateListView,
    LandCreateView,
    LandDetailView,
    LandListView,
    LandImageCreateView,
    LandImageDetailView,
    LandImageListView,
    LandReviewCreateView,
    LandReviewDetailView,
    LandReviewListView,
    LandVideoCreateView,
    LandVideoListView,
    OpenDataTimeListView,
    OpenDateTimeCreateView,
    OpenDateTimeDetailView,
    SaveLandAPIView,
    SaveLandCreateView,
    SaveLandDetailView,
    SaveLandListView,
)

from django.urls import path

urlpatterns = [
    path("lands/", LandListView.as_view(), name="lands"),
    path(
        "user-profile/<int:profile_pk>/create-land/",
        LandCreateView.as_view(),
        name="create-land",
    ),
    path(
        "user-profile/<int:profile_pk>/lands/",
        LandListView.as_view(),
        name="list-lands",
    ),
    path("lands/<slug>/", LandDetailView.as_view(), name="land"),
    path(
        "lands/<int:land_pk>/create-land-image/",
        LandImageCreateView.as_view(),
        name="create-land-image",
    ),
    path("lands/<int:pk>/save-like/", SaveLandAPIView.as_view(), name="save-like"),
    path("land-images/", LandImageListView.as_view(), name="all-land-images"),
    path(
        "lands/<int:land_pk>/land-images/",
        LandImageListView.as_view(),
        name="land-images",
    ),
    path(
        "lands/<int:land_pk>/land-images/<int:pk>/",
        LandImageDetailView.as_view(),
        name="land-image",
    ),
    path(
        "lands/<int:land_pk>/create-land-video/",
        LandVideoCreateView.as_view(),
        name="create-land-video",
    ),
    path("land-videos/", LandVideoListView.as_view(), name="all-land-videos"),
    path(
        "lands/<int:land_pk>/land-videos/",
        LandVideoListView.as_view(),
        name="land-videos",
    ),
    path(
        "lands/<int:land_pk>/create-land-review/",
        LandReviewCreateView.as_view(),
        name="create-land-review",
    ),
    path("land-reviews/", LandReviewListView.as_view(), name="land-reviews"),
    path(
        "lands/<int:land_pk>/land-reviews/",
        LandReviewListView.as_view(),
        name="land-list-reviews",
    ),
    path(
        "lands/<int:land_pk>/land-reviews/<int:pk>/",
        LandReviewDetailView.as_view(),
        name="land-review",
    ),
    path(
        "lands/<int:land_pk>/create-open-date-time/",
        OpenDateTimeCreateView.as_view(),
        name="create-open-date-time",
    ),
    path(
        "lands/<int:land_pk>/open-date-time/<int:pk>/",
        OpenDateTimeDetailView.as_view(),
        name="open-date-time",
    ),
    path(
        "lands/<int:land_pk>/open-date-time/",
        OpenDataTimeListView.as_view(),
        name="list-open-date-time",
    ),
    path(
        "land-contact-numbers/", ContactNumberListView.as_view(), name="contact-numbers"
    ),
    path(
        "lands/<int:land_pk>/contact-numbers/",
        ContactNumberListView.as_view(),
        name="list-land-contact-number",
    ),
    path(
        "lands/<int:land_pk>/contact-numbers/<int:pk>/",
        ContactNumberDetailView.as_view(),
        name="land-number",
    ),
    path(
        "lands/<int:land_pk>/create-contact-number/",
        ContactNumberCreateView.as_view(),
        name="create-contact-number",
    ),
    path(
        "lands/<int:land_pk>/land-coordinate/<int:pk>/",
        LandCoordinateDetailView.as_view(),
        name="land-coordinate",
    ),
    path(
        "lands/<int:land_pk>/create-land-coordinate/",
        LandCoordinateCreateView.as_view(),
        name="create-land-coordinate",
    ),
    path(
        "lands/<int:land_pk>/land-coordinate/",
        LandCoordinateListView.as_view(),
        name="list-land-coordinate",
    ),
    path(
        "user-profile/<int:profile_pk>/lands/<int:land_pk>/save/",
        SaveLandCreateView.as_view(),
        name="save-land",
    ),
    path(
        "user-saved-lands/",
        SaveLandListView.as_view(),
        name="user-saved-lands",
    ),
    path(
        "user-saved-lands/<int:pk>/",
        SaveLandDetailView.as_view(),
        name="user-saved-detail-lands",
    ),
]
