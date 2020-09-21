from django.db import models
from profiles.models import Profile
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.utils import timezone
from PIL import Image
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

HOME_STATUS = ((0, "For Rent"), (1, "For Sale"))


class Home(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="homes")
    slug = models.SlugField(max_length=255, blank=True, null=True)
    home_price = models.IntegerField()
    home_type = models.CharField(max_length=250, blank=True)
    virtual_tour_url = models.URLField(blank=True)
    hoa_dues = models.IntegerField(blank=True)
    address = models.CharField(max_length=350, blank=True)
    city = models.CharField(max_length=150, blank=True)
    number_bedrooms = models.IntegerField(blank=True)
    number_bathrooms = models.IntegerField(blank=True)
    home_size = models.IntegerField(blank=True)
    year_built = models.IntegerField(blank=True)
    describe_home = models.TextField(blank=True)
    related_website = models.URLField(blank=True)
    love_about_home = models.TextField(blank=True)
    home_status = models.CharField(max_length=1, choices=HOME_STATUS, blank=True)
    date_posted = models.DateField(default=timezone.now)
    saves = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="saves")

    def __str__(self):
        return self.user.username


class HomeImage(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="home_images")
    home_image = models.ImageField(blank=True, null=True, upload_to="home_images")

    def __str__(self):
        return str(self.home)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.home_image.path)

        if img.height > 1080 or img.width > 1080:
            output_size = (1080, 1080)
            img.thumbnail(output_size)
            img.save(self.home_image.path)


class HomeVideo(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="home_videos")
    home_video = models.FileField(
        blank=True,
        null=True,
        upload_to="home_videos",
        validators=[FileExtensionValidator(allowed_extensions=["mp4"])],
    )

    def __str__(self):
        return str(self.home)


class OpenDateTime(models.Model):
    home = models.ForeignKey(
        Home, on_delete=models.CASCADE, related_name="open_date_time"
    )
    open_day = models.CharField(max_length=1, choices=DAYS_OF_WEEK, blank=True)
    open_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.home)


class ContactNumber(models.Model):
    home = models.ForeignKey(
        Home, on_delete=models.CASCADE, related_name="contact_number"
    )
    number = PhoneNumberField(blank=True)

    def __str__(self):
        return str(self.number)


class HomeCoordinate(models.Model):
    home = models.ForeignKey(
        Home, on_delete=models.CASCADE, related_name="home_coordinate"
    )
    longitude = models.FloatField(blank=True)
    latitude = models.FloatField(blank=True)

    def __str__(self):
        return f"{self.longitude}, {self.latitude}"


class HomeReview(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.IntegerField(
        validators=(MinValueValidator(0), MaxValueValidator(5)), blank=True, null=True
    )
    message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.rate)


class RoomFeature(models.Model):
    home = models.ForeignKey(
        Home, on_delete=models.CASCADE, related_name="room_features"
    )
    room_feature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.home)


class KitchenFeature(models.Model):
    home = models.ForeignKey(
        Home, on_delete=models.CASCADE, related_name="kitchen_features"
    )
    kitchen_feature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.home)


class GeneralHomeFeatures(models.Model):
    home = models.ForeignKey(
        Home, on_delete=models.CASCADE, related_name="general_home_features"
    )
    home_feature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.home)

    def save(self, *args, **kwargs):
        self.home_feature = self.home_feature.lower()
        return super().save(*args, **kwargs)


class SittingRoomFeature(models.Model):
    home = models.ForeignKey(
        Home, on_delete=models.CASCADE, related_name="sitting_room_features"
    )
    sitting_room_feature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.home)


class SaveHome(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="saved_homes"
    )

    def __str__(self):
        return str(self.home)