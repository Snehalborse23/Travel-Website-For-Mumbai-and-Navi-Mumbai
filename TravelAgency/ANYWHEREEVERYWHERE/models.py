from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    # Add any other fields you need
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

    def __str__(self):
        return self.username
    
# class Rating(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     stars = models.IntegerField()

#     def __str__(self):
#         return f'{self.user} rated {self.stars} stars'    
    
class Location(models.Model):
    name = models.CharField(max_length=255)


class Review(models.Model):
    location = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return f"{self.location} - {self.user.username}"
