from django.shortcuts import render, redirect
from .models import user, competition, entry
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from app.serializers import userserializer, competitionserializer, entryserializer
from rest_framework.response import Response

# Create your views here.


# Operations for User
@api_view(["POST"])
def create_user(request, id=None):
    '''
    This functions creates a new user in database with the given parameters from userserializer and Posts it
    '''
    if request.method == "POST":
        create = userserializer(data=request.data)           # Stores the data from userserialzer in a variable
        if create.is_valid():
            create.save()
            return Response("User Created Successfully")
        return Response(create.errors)                       # Returns the error


@api_view(["GET"])
def retrieve_user(request, id=None):
    '''
    This function returns all the users as output if id is not specified and if it is, then returns a user with that particular id
    '''
    user_id = id
    if request.method == "GET":
        if id is not None:
            u = user.objects.get(id=user_id)  # Fetches field with a particular id
            serializer = userserializer(u)
            return Response(serializer.data)
    u = user.objects.all()  # Takes all the users
    serializer = userserializer(u, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
def update_user(request, id=None):
    '''
    This function takes an id and alters the existing fields with the new data provided by the user. If the data is in valid format, it is saved otherwise error is displayed
    '''
    user_id = id
    if request.method == "PUT":
        if id is not None:
            usr = user.objects.get(id=user_id)
            update = userserializer(usr, data=request.data, partial=True)  # Requests data from the userserializer and also supports partial updation
            if update.is_valid():
                update.save()
                return Response("Updated Successfully")
            else:
                return Response(update.errors)


@api_view(["DELETE"])
@csrf_exempt
def delete_user(request, abc):
    '''
    This function takes an id of a user and performs the delete operation using .delete()
    '''
    v = user.objects.get(id=abc)                        # Takes an object with a unique id
    v.delete()                                      # Used to delete a field
    return Response("User Deleted Successfully")


# Operations for Competition
@api_view(["POST"])
def create_competition(request, id=None):
    if request.method == "POST":
        create = competitionserializer(data=request.data)
        if create.is_valid():                                   #Checks validation
            create.save()
            return Response("Competition Created Successfully")
        return Response(create.errors)


@api_view(["GET"])
def retrieve_competition(request, id=None):
    competition_id = id                             #Stored the id in a variable
    if request.method == "GET":
        if id is not None:                          #If id is an integer value and not none
            u = competition.objects.get(id=competition_id)
            serializer = competitionserializer(u)
            return Response(serializer.data)
    u = competition.objects.all()
    serializer = competitionserializer(u, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
def update_competition(request, id=None):
    competition_id = id
    if request.method == "PUT":                         #PUT method is used for update operation
        if id is not None:
            comp = competition.objects.get(id=competition_id)           #Fetches a field from competition with a unique id
            update = competitionserializer(comp, data=request.data, partial=True)
            if update.is_valid():
                update.save()
                return Response("Updated Successfully")
            else:
                return Response(update.errors)


@api_view(["DELETE"])
@csrf_exempt
def delete_competition(request, abc):
    v = competition.objects.get(id=abc)
    v.delete()
    return Response("Competition Deleted Successfully")


# Operations for Entry
@api_view(["POST"])
def create_entry(request, id=None):
    if request.method == "POST":
        create = entryserializer(data=request.data)
        if create.is_valid():
            create.save()
            return Response("Entry Created Successfully")
        return Response(create.errors)


@api_view(["GET"])
def retrieve_entry(request, id=None):
    entry_id = id
    if request.method == "GET":
        if id is not None:
            u = entry.objects.get(id=entry_id)
            serializer = entryserializer(u)
            return Response(serializer.data)
    u = entry.objects.all()
    serializer = entryserializer(u, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
def update_entry(request, id=None):
    entry_id = id
    if request.method == "PUT":
        if id is not None:
            ent = entry.objects.get(id=entry_id)
            update = entryserializer(ent, data=request.data, partial=True)
            if update.is_valid():
                update.save()
                return Response("Entry Updated Successfully")
            else:
                return Response(update.errors)


@api_view(["DELETE"])
@csrf_exempt
def delete_entry(request, abc):
    v = entry.objects.get(id=abc)
    v.delete()
    return Response("Entry Deleted Successfully")
