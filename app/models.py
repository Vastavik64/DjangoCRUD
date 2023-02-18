from django.db import models

# Create your models here.
class user(models.Model):
    '''
    This class creates a model user in django database with the fields defined
    '''
    id = models.AutoField(primary_key = True, auto_created=True)
    name = models.TextField()
    birthdate = models.DateField()
    gender = models.TextField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):                          #This method defines an instance of a class which is displayed as a string
        return self.name


class competition(models.Model):
    '''
    This class creates a model competition in django database with the fields defined
    '''
    id = models.AutoField(primary_key = True, auto_created=True)
    name = models.TextField()
    status = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=100)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE, null=True)          #Foreign Key is used to connect two models

    def __str__(self):
        return self.name



class entry(models.Model):
    '''
    This class creates a model entry in django database with the fields defined
    '''
    id = models.AutoField(primary_key = True, auto_created=True)
    title = models.TextField()
    topic = models.TextField()
    state = models.TextField()
    country = models.TextField()
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    competition_id = models.ForeignKey(competition, on_delete=models.CASCADE, null=True)
