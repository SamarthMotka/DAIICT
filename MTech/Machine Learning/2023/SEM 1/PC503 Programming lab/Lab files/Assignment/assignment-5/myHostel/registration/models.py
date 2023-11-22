# registration/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    permanent_address = models.TextField()
    college_id = models.CharField(max_length=20)
    college_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    room_type = models.CharField(max_length=10, choices=[('AC', 'AC'), ('NON-AC', 'NON-AC')])
    food_preference = models.CharField(max_length=10, choices=[('food', 'Food'), ('not-food', 'Not Food')])

    def __str__(self):
        return self.user.username
