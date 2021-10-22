from re import I, S
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view

from user.models import User
from .serializers import TeamSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team


def index(request):
    return HttpResponse("Hello World")


class GetAllTeams(APIView):
    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


class TeamDetails(APIView):
    def get_object(self, id):
        try:
            return Team.objects.filter(id=id)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        teams = self.get_object(id)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def api_get_all(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)


@api_view(['PUT', ])
def api_update_team(request, slug):
    try:
        teams = Team.objects.all()
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TeamSerializer(teams, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update successfully"
            return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST', ])
def api_create_team(request):

    if request.method == 'POST':
        serializer = TeamSerializer(Team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
