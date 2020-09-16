from django.db import models
from django.conf import settings
from PIL import Image


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True)
    profile_pic = models.ImageField(
        default="profile_pics/profile_pic.png",
        upload_to="profile_pics",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.home_image.path)
