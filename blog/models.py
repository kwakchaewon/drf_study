from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    first_name= None
    birth = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(
        max_length=13,
        blank=True,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['last_name', 'phone', 'email', 'birth']

    class Meta:
        db_table = 'user'


class BoardCategories(models.Model):
    category_type = models.CharField(max_length=45)
    category_code= models.CharField(max_length=100)
    category_name= models.CharField(max_length=100)
    list_count = models.IntegerField(blank=True, null=True)
    authority = models.IntegerField(blank=True, null=True)
    creation_date = models.DateField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'board_categories'

class Board(models.Model):
    category = models.ForeignKey(BoardCategories, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    conntents = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(blank=True, default=0)
    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True)

    class Meta:
        db_table = 'boards'

class BoardReplies(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField(blank=True, null=True)
    contents = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    refer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'board_replies'

class BoardLikes(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'board_likes'

