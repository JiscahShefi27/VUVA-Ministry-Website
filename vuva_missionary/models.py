from django.db import models
from vuva_admin.models import Missionary
from django.utils.timezone import now
# Create your models here.
class MissionaryPrayerRequest(models.Model):
    request = models.TextField()  # Stores the prayer request text
    submitted_at = models.DateTimeField(default=now)  # Timestamp of submission

    def __str__(self):
        return f"Prayer Request {self.id} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
    
class MissionaryReport(models.Model):
    missionary = models.ForeignKey(
        Missionary,
        on_delete=models.CASCADE
    )

    report_file = models.FileField(
        upload_to='missionary_reports/'
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.missionary.username} Report"