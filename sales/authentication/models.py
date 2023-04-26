from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

import uuid


class ResetPaswordRequest(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="change_password_requests", on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
