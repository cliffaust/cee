import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits

STRING_LENGTH = 6

VIDEO_FILE_FORMATS = [
    "MP4",
    "m4v",
    "webm",
    "mkv",
    "flv",
    "flc",
    "vob",
    "ogv",
    "ogg",
    "drc",
    "gif",
    "gifv",
    "mng",
    "avi",
    "MTS",
    "M2TS",
    "TS",
    "mov",
    "qt",
    "wmv",
    "yuv",
    "rm",
    "rmvb",
    "viv",
    "asf",
    "amv",
    "m4p",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "m2v",
    "svi",
    "3gp",
    "3g2",
    "mxf",
    "roq",
    "nsv",
    "f4v",
    "f4p",
    "f4a",
    "f4b",
]


def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))


def home_image_thumbnail(instance, filename):
    return f"home_images/{instance.home.id}/{filename}"


def home_video_thumbnail(instance, filename):
    return f"home_videos/{instance.home.id}/{filename}"


def land_image_thumbnail(instance, filename):
    return f"land_images/{instance.land.id}/{filename}"


def land_video_thumbnail(instance, filename):
    return f"land_videos/{instance.land.id}/{filename}"


def profile_image_thumbnail(instance, filename):
    return f"profile_images/{instance.user.id}/{filename}"