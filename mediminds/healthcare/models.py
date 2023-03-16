from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    
class RoleRegistration(models.Model):
    full_name = models.CharField(max_length=100),
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    role = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s %s" %(self.full_name, self.username, self.role)