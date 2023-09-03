from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint, choice
from django.db.models import QuerySet
from extention.name_changer import upload_user_img_path

# Create your models here.

def unique_id() -> str:
    random_number: int = randint(10_000, 999_999_999)
    final_randome_number: str = str(choice([random_number, -random_number]))
    all_user_id: QuerySet[User] = User.objects.all()
    user_id = list(map(lambda user: user.user_id, all_user_id))
    while final_randome_number in user_id:
        random_number: int = randint(10_000, 999_999_999)
        final_randome_number: str = str(choice([random_number, -random_number]))
        
    return final_randome_number


class User(AbstractUser):
    user_id = models.CharField(
        max_length=12,
        default=unique_id,
        unique=True, 
        null=False, 
        blank=False,
    )
    profile_picture = models.ImageField(
        upload_to=upload_user_img_path,
        blank=True,
        null=True,
    )
    user_bio = models.CharField(
        max_length=512,
        null=True,
        blank=True,
    )


