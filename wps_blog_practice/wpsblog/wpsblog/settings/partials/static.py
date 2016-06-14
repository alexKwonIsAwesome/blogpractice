import os

from .base import PROJECT_ROOT_DIR


STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(
        PROJECT_ROOT_DIR,
        "dist",
        "media",
    )
MEDIA_URL = '/media/'

