from .views import (
    HomeCreateView,
    HomeListView,
    HomeDetailView,
    HomeImageCreateView,
    OpenDateTimeCreateView,
    ContactNumberCreateView,
    HomeCoordinateCreateView,
    OpenDateTimeDetailView,
    HomeReviewCreateView,
    HomeReviewListView,
    HomeReviewDetailView,
    ContactNumberListView,
    ContactNumberDetailView,
    HomeImageListView,
    HomeImageDetailView,
    HomeCoordinateDetailView,
    RoomFeatureCreateView,
    KitchenFeatureCreateView,
    SittingRoomFeatureCreateView,
    SaveHomeCreateView,
    SaveHomeAPIView,
    SaveHomeListView,
    SaveHomeDetailView,
    GeneralHomeFeaturesCreateView,
    GeneralHomeFeaturesListView,
    HomeCoordinateListView,
    KitchenFeatureListView,
    OpenDataTimeListView,
    RoomFeatureListView,
    SittingRoomFeatureListView,
    HomeVideoCreateView,
    HomeVideoListView,
    HomeVideoSerializer,
    HomeVideoDetailView,
)
from django.urls import path


urlpatterns = [
    path(
        "user-profile/<int:profile_pk>/create-home/",
        HomeCreateView.as_view(),
        name="create-home",
    ),
    path("homes/", HomeListView.as_view(), name="homes"),
    path(
        "user-profile/<int:profile_pk>/homes/",
        HomeListView.as_view(),
        name="list-homes",
    ),
    path("homes/<slug>/", HomeDetailView.as_view(), name="home"),
    path(
        "homes/<int:home_pk>/create-home-image/",
        HomeImageCreateView.as_view(),
        name="create-home-image",
    ),
    path("homes/<int:pk>/save-like/", SaveHomeAPIView.as_view(), name="save-like"),
    path("home-images/", HomeImageListView.as_view(), name="all-home-images"),
    path(
        "homes/<int:home_pk>/home-images/",
        HomeImageListView.as_view(),
        name="home-images",
    ),
    path(
        "homes/<int:home_pk>/home-images/<int:pk>/",
        HomeImageDetailView.as_view(),
        name="home-image",
    ),
    path(
        "homes/<int:home_pk>/home-videos/<int:pk>/",
        HomeVideoDetailView.as_view(),
        name="home-video",
    ),
    path(
        "homes/<int:home_pk>/create-home-video/",
        HomeVideoCreateView.as_view(),
        name="create-home-video",
    ),
    path("home-videos/", HomeVideoListView.as_view(), name="all-home-videos"),
    path(
        "homes/<int:home_pk>/home-videos/",
        HomeVideoListView.as_view(),
        name="home-videos",
    ),
    path(
        "homes/<int:home_pk>/create-home-review/",
        HomeReviewCreateView.as_view(),
        name="create-home-review",
    ),
    path("home-reviews/", HomeReviewListView.as_view(), name="home-reviews"),
    path(
        "homes/<int:home_pk>/home-reviews/",
        HomeReviewListView.as_view(),
        name="home-list-reviews",
    ),
    path(
        "homes/<int:home_pk>/home-reviews/<int:pk>/",
        HomeReviewDetailView.as_view(),
        name="home-review",
    ),
    path(
        "homes/<int:home_pk>/create-open-date-time/",
        OpenDateTimeCreateView.as_view(),
        name="create-open-date-time",
    ),
    path(
        "homes/<int:home_pk>/open-date-time/<int:pk>/",
        OpenDateTimeDetailView.as_view(),
        name="open-date-time",
    ),
    path(
        "homes/<int:home_pk>/open-date-time/",
        OpenDataTimeListView.as_view(),
        name="list-open-date-time",
    ),
    path(
        "home-contact-numbers/",
        ContactNumberListView.as_view(),
        name="home-contact-numbers",
    ),
    path(
        "homes/<int:home_pk>/contact-numbers/",
        ContactNumberListView.as_view(),
        name="list-home-contact-number",
    ),
    path(
        "homes/<int:home_pk>/contact-numbers/<int:pk>/",
        ContactNumberDetailView.as_view(),
        name="home-number",
    ),
    path(
        "homes/<int:home_pk>/create-contact-number/",
        ContactNumberCreateView.as_view(),
        name="create-contact-number",
    ),
    path(
        "homes/<int:home_pk>/home-coordinate/<int:pk>/",
        HomeCoordinateDetailView.as_view(),
        name="home-coordinate",
    ),
    path(
        "homes/<int:home_pk>/create-home-coordinate/",
        HomeCoordinateCreateView.as_view(),
        name="create-home-coordinate",
    ),
    path(
        "homes/<int:home_pk>/home-coordinate/",
        HomeCoordinateListView.as_view(),
        name="list-home-coordinate",
    ),
    path(
        "homes/<int:home_pk>/create-room-feature/",
        RoomFeatureCreateView.as_view(),
        name="create-room-feature",
    ),
    path(
        "homes/<int:home_pk>/room-features/",
        RoomFeatureListView.as_view(),
        name="list-room-features",
    ),
    path(
        "homes/<int:home_pk>/create-general-home-feature/",
        GeneralHomeFeaturesCreateView.as_view(),
        name="create-general-home-feature",
    ),
    path(
        "homes/<int:home_pk>/general-home-features/",
        GeneralHomeFeaturesListView.as_view(),
        name="list-general-home-feature",
    ),
    path(
        "homes/<int:home_pk>/create-kitchen-feature/",
        KitchenFeatureCreateView.as_view(),
        name="create-kitchen-feature",
    ),
    path(
        "homes/<int:home_pk>/kitchen-features/",
        KitchenFeatureListView.as_view(),
        name="list-kitchen-feature",
    ),
    path(
        "homes/<int:home_pk>/create-sitting-room-feature/",
        SittingRoomFeatureCreateView.as_view(),
        name="create-sitting-room-feature",
    ),
    path(
        "homes/<int:home_pk>/sitting-room-features/",
        SittingRoomFeatureListView.as_view(),
        name="list-sitting-room-feature",
    ),
    path(
        "user-profile/<int:profile_pk>/homes/<int:home_pk>/save/",
        SaveHomeCreateView.as_view(),
        name="save-home",
    ),
    path(
        "user-saved-homes/",
        SaveHomeListView.as_view(),
        name="user-saved-homes",
    ),
    path(
        "user-saved-homes/<int:pk>/",
        SaveHomeDetailView.as_view(),
        name="user-saved-detail-homes",
    ),
]
