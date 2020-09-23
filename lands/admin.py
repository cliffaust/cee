from django.contrib import admin
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

admin.site.register(ContactNumber)
admin.site.register(Land)
admin.site.register(LandCoordinate)
admin.site.register(LandImage)
admin.site.register(LandVideo)
admin.site.register(LandReview)
admin.site.register(SaveLand)
admin.site.register(OpenDateTime)
