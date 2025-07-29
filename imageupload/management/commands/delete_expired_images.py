from django.core.management.base import BaseCommand
from django.utils.timezone import now
from imageupload.models import Image

class Command(BaseCommand):
    help = 'Delete images that have expired based on retention_days'

    def handle(self, *args, **options):
        images = Image.objects.all()
        deleted_count = 0
        for image in images:
            expiration = image.expiration_date()
            if expiration and expiration < now():
                image.image.delete(save=False)  # Delete the file
                image.delete()  # Delete the database record
                deleted_count += 1
        self.stdout.write(self.style.SUCCESS(f'Deleted {deleted_count} expired images.'))
