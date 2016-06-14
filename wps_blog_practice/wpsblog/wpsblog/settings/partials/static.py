import os

from .base import PROJECT_ROOT_URL


STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(
        PROJECT_ROOT_URL,
        "dist",
        "media",
    )

