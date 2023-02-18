from rest_framework import serializers
from django.db import models
from .models import user, competition, entry

class userserializer(serializers.Serializer):
    '''
    This class inherits from serializers class and defines the fields name birthdate and gender for various operations
    '''
    name = serializers.CharField()
    birthdate = serializers.DateField()
    gender = serializers.CharField(max_length=8)

    def create(self, validated_data):
        return user.objects.create(**validated_data)                #Creates a new user


    def update(self, instance, validated_data):
        '''
        This function takes three input arguments and stores the data entered by the user into the respective fields present in database
        '''
        instance.name = validated_data.get('name', instance.name)
        instance.birthdate = validated_data.get('birthdate',instance.birthdate)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()                         #Saves the data
        return instance
    

class competitionserializer(serializers.Serializer):
    '''
    This class creates serializer for competition with the input fields
    '''
    name = serializers.CharField()
    status = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=100)
    user_id = serializers.PrimaryKeyRelatedField(queryset=user.objects.all())       #Froms the relation between user and competition model with the help of userid

    def create(self, validated_data):
        '''
        It takes validated data as a parameter and creates an object in competition
        '''
        return competition.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status',instance.status)
        instance.description = validated_data.get('description', instance.description)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance
    
class entryserializer(serializers.Serializer):
    title = serializers.CharField()
    topic = serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField()
    competition_id = serializers.PrimaryKeyRelatedField(queryset=competition.objects.all())    #Connects entry model with competition

    def create(self, validated_data):
        return entry.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.topic = validated_data.get('topic',instance.topic)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.competition_id = validated_data.get('competition_id', instance.competition_id) 
        instance.save()
        return instance