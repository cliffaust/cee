from django.contrib import admin
from .models import (
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

admin.site.register(Home)
admin.site.register(HomeImage)
admin.site.register(HomeCoordinate)
admin.site.register(OpenDateTime)
admin.site.register(ContactNumber)
admin.site.register(HomeReview)
admin.site.register(RoomFeature)
admin.site.register(KitchenFeature)
admin.site.register(SittingRoomFeature)
admin.site.register(SaveHome)
admin.site.register(GeneralHomeFeatures)
admin.site.register(HomeVideo)
