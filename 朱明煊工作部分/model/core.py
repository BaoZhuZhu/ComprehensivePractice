import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "model.settings")
django.setup()
from comprehensivePractice.models import UserInfo