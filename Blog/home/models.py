from django.db import models
from django.conf import settings

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    mode = models.ForeignKey('Mode',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    #updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title

class Mode(models.Model):
    name = models.CharField(max_length = 8)
    def __str__(self):
        return self.name
