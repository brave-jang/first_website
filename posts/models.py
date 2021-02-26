from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Posts(BaseModel):

    class CountryChoice(models.TextChoices):
        KOREA = "K", "국내"
        WORLD = "W", "해외"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts_user", on_delete=CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True)
    content = models.TextField()
    content_img = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    post_url = models.URLField()
    country = models.CharField(max_length=2, choices=CountryChoice.choices)
    category = models.ManyToManyField("Category")
    tag = models.ManyToManyField("Tag", blank=True)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="like_user_set")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Posts"


class Category(BaseModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Category"


class Tag(BaseModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name