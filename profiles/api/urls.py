from django.urls import path
from .views import (
    ProfileListView,
    UserProfileView,
    UserProfileDetailView,
)


urlpatterns = [
    path("profiles/", ProfileListView.as_view(), name="profiles"),
    path("user-profile/", UserProfileView.as_view(), name="user-profile"),
    path(
        "user-profile/<int:pk>/",
        UserProfileDetailView.as_view(),
        name="user-profile-detail",
    ),
]