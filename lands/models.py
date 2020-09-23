from django.db import models
from django.conf import settings
from profiles.models import Profile
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
from core.utils import land_image_thumbnail, land_video_thumbnail, VIDEO_FILE_FORMATS
from django.core.validators import FileExtensionValidator


DAYS_OF_WEEK = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
)


class Land(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="lands")
    slug = models.SlugField(max_length=255, unique=True)
    land_price = models.IntegerField()
    virtual_tour_url = models.URLField(blank=True)
    land_dues = models.IntegerField(blank=True)
    address = models.CharField(max_length=350, blank=True)
    city = models.CharField(max_length=150, blank=True)
    land_size = models.IntegerField(blank=True)
    describe_land = models.TextField(blank=True)
    related_website = models.URLField(blank=True)
    love_about_land = models.TextField(blank=True)
    date_posted = models.DateField(default=timezone.now)
    saves = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="land_saves")

    def __str__(self):
        return str(self.user)


class LandImage(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name="land_images")
    land_image = models.ImageField(
        blank=True, null=True, upload_to=land_image_thumbnail
    )

    def __str__(self):
        return str(self.land)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.land_image.path)

        if img.height > 1080 or img.width > 1080:
            output_size = (1080, 1080)
            img.thumbnail(output_size)
            img.save(self.land_image.path)


class LandVideo(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name="land_videos")
    land_video = models.FileField(
        blank=True,
        null=True,
        upload_to=land_video_thumbnail,
        validators=[
            FileExtensionValidator(
                allowed_extensions=VIDEO_FILE_FORMATS, message="unsupported file format"
            )
        ],
    )

    def __str__(self):
        return str(self.land)


class OpenDateTime(models.Model):
    land = models.ForeignKey(
        Land, on_delete=models.CASCADE, related_name="open_date_time"
    )
    open_day = models.CharField(max_length=1, choices=DAYS_OF_WEEK, blank=True)
    open_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.land)


class ContactNumber(models.Model):
    land = models.ForeignKey(
        Land, on_delete=models.CASCADE, related_name="contact_numbers"
    )
    number = PhoneNumberField(blank=True)

    def __str__(self):
        return str(self.number)


class LandCoordinate(models.Model):
    land = models.ForeignKey(
        Land, on_delete=models.CASCADE, related_name="land_coordinate"
    )
    longitude = models.FloatField(blank=True)
    latitude = models.FloatField(blank=True)

    def __str__(self):
        return f"{self.longitude}, {self.latitude}"


class LandReview(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.IntegerField(
        validators=(MinValueValidator(0), MaxValueValidator(5)), blank=True, null=True
    )
    message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.rate)


class SaveLand(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="saved_lands"
    )

    def __str__(self):
        return str(self.land)