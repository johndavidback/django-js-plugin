from django.db import models

# Create your models here.
class ClickTrack(models.Model):
    page_id = models.IntegerField(max_length=10)
    clicks = models.IntegerField(max_length=7)

    def add_click(self):
        self.clicks += 1
        self.save()
