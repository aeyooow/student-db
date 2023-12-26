from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, db_index=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

class User(AbstractUser):
    GENDER =(
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    student_id = models.IntegerField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    birthdate = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=6, null=False, blank=False, choices=GENDER)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='studentapp_user_groups',  # Updated related_name
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='studentapp_user_permissions',  # Updated related_name
        related_query_name='user',
    )
    def __str__(self):
        return self.username

