import os
import uuid
from django.db import models
from django.contrib.auth.models import User

def unique_file_path(instance, filename):
    ext = filename.split('.')[-1]
    # generate unique filename with uuid4
    unique_filename = f"{uuid.uuid4().hex}.{ext}"
    from django.conf import settings
    return os.path.join(settings.MEDIA_ROOT, 'uploaded_images', unique_filename)

class Image(models.Model):
    image = models.ImageField(upload_to=unique_file_path)
    name = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    retention_days = models.PositiveIntegerField(null=True, blank=True, help_text="Retention period in days (max 30). Null means unlimited for admins.")

    def __str__(self):
        return self.name

    def get_file_size(self):
        if self.image and hasattr(self.image, 'size'):
            return self.image.size
        return 0

    def expiration_date(self):
        if self.retention_days is None or self.retention_days == 0:
            return None
        from django.utils.timezone import timedelta
        return self.uploaded_at + timedelta(days=self.retention_days)
