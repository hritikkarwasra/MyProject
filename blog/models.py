from django.db import models
import uuid
import datetime
# Create your models here.

class Blogs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, blank= False)
    author_name = models.CharField(max_length=255, blank= False, null= False)
    content = models.TextField(blank=False, null=False)
    publication_date = models.DateField(auto_now_add= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    comment = models.TextField(null=False, blank=False)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
