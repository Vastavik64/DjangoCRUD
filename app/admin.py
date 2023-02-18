from django.contrib import admin

# Register your models here.
from .models import user, competition, entry

# Register your models here.
@admin.register(user)
class useradmin(admin.ModelAdmin):
    '''
    It composes the created user model to be reflected in database
    '''
    list_display = ['id','name','birthdate','gender','created_at','updated_at','is_active','is_delete']

@admin.register(competition)
class competitionadmin(admin.ModelAdmin):
    '''
    Created competition model is composed to be reflected in database
    '''
    list_display = ['id','name','status','is_active','is_delete','updated_at','is_active','is_delete','created_at','updated_at','description','user_id']


@admin.register(entry)
class entryadmin(admin.ModelAdmin):
    '''
    Created entry model is registered to be reflected in database
    '''
    list_display = ['id','title','topic','state','country','is_delete','created_at','updated_at','competition_id']