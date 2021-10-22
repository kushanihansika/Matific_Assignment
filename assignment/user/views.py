from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view

from role.models import Role
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team, User


@api_view(['POST', ])
def api_register_user(request):

    team = Team.objects.get(id=request.POST.get("team"))
    role = Role.objects.get(id=request.POST.get('role'))
    user = User(team=team, role=role)


    if request.method == 'POST':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

# if user start to play match then update users role to 4
@api_view(['POST',])
def api_update_match_player(request,slug):
    # get match player role
    role =Role.objects.get(id=4)
    user =User(role=role)
    if request.method == 'POST':
        serializer = UserSerializer(user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET',])
def api_get_high_score_players(request):
    users = User.objects.filter()  