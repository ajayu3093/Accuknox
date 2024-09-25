from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
from django.dispatch import receiver
from django.conf import settings

# user = settings.AUTH_USER_MODEL

# @receiver(pre_save, sender=user)
# def create_user_profile(sender, instance,*args,**kwargs):
#     print("Testing", instance.id)
    
# @receiver(post_save, sender=user)
# def create_user_profile(sender, instance, created, *args, **kwargs):
#     if created:
#         print("User Created",instance.id)

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender= User)
def datapost(sender,instance,created,*args,**kwargs):
    if created:
        print("user created",instance.username)
    else:
        print(instance.username,"just modified")

class blog(models.Model):
    Blog_Title= models.CharField(max_length=120)
    Author = models.CharField(max_length=50,null=False)
    notify_users = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Blog_Title

@receiver(pre_save, sender=blog)
def blog_pre_save(sender, instance,*args,**kwargs):
    print("Creating a New Blog")

@receiver(post_save,sender = blog)
def post_save_blog(sender, instance, created,*args,**kwargs):
    if instance.notify_users or created:
        print("notify users")
        instance.notify_users = False
        if created:
            print("New Blog Created")
@receiver(pre_delete,sender=blog)
def blog_delete(sender,instance,*args,**kwargs):
    print(f"{instance.Blog_Title} will be deleted, it's an gaint data tooks long time")

@receiver(post_delete, sender= blog)
def blog_post_delete(sender,instance, *args,**kwargs):
    print(f"{instance.Blog_Title} has been deleted")
        
