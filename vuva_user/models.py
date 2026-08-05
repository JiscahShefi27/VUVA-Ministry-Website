from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()

class CounselBooking(models.Model):

    COUNSELING_TYPES = [
        ("family", "Family Counselling"),
        ("marriage", "Marriage Counselling"),
        ("education", "Educational Counselling"),
        ("mental", "Mental Health Counselling"),
        ("other", "Other"),
    ]

    COUNSELOR_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("any", "Any"),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    booking_date = models.DateField()
    counseling_type = models.CharField(max_length=50, choices=COUNSELING_TYPES)
    counselor = models.CharField(max_length=20, choices=COUNSELOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.booking_date}"
    
class UserPrayerRequest(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    request = models.TextField()
    submitted_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Prayer Request {self.id} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
