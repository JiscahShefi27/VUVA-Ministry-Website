from django.db import models

#Admin Update on ministry details
class AdminStats(models.Model):
    total_villages = models.PositiveIntegerField(default=0)
    total_churches = models.PositiveIntegerField(default=0)
    total_missionaries = models.PositiveIntegerField(default=0)

    # (optional)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "VUVA Ministry Stats"



class Event(models.Model):
    image = models.ImageField(upload_to='events_images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Missionary(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=128)  # store hashed password

    def __str__(self):
        return self.username
