from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models  import ContentType
# Create your models here.
class User(AbstractUser):
    pass



class CategoryBlog(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return f"{self.name}"
    

class BLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE)
    name = models.CharField(max_length =150, blank=True, null=True)
    Text  = models.TextField(max_length=1000 )
    image = models.ImageField(upload_to="image", blank=True)
    date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    
    
   

    def __str__(self):
        return f"{self.user.username}"
    

class Comment(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BLog, on_delete=models.CASCADE)
    content = models.CharField(max_length=234 , blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
    


    
    
    