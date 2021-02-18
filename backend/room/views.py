from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions, status
from room.models import Team, Player
from room.serializers import (PlayerPostSerializers, PlayerSerializers,
                              TeamPostSerializers, TeamSerializers)


class TeamView(APIView):
    """ Team profile """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = Team.objects.filter(user=request.user)
        serializer = TeamSerializers(profile, many=True)
        return Response({"response": serializer.data})

    def post(self, request):
        team_data = TeamPostSerializers(data=request.data)
        profile = Team.objects.filter(user=request.user)
        print(team_data)
        if team_data.is_valid():
            if profile:
                return Response({"status": "The team is not first"})
            else:
                team_data.save(user=request.user)
            return Response({"status": True})
        else:
            return Response(team_data.errors)

    def put(self, request):
        saved_article = get_object_or_404(Team.objects.filter(user=request.user))
        data = request.data.get('team')
        serializer = TeamPostSerializers(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            team_saved = serializer.save()
        return Response({"success": "Team '{}' updated successfully".format(team_saved.name)})


class PlayerView(APIView):
    """ Player  """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        player_profile = Player.objects.filter(user=request.user)
        serializer = PlayerSerializers(player_profile, many=True)
        return Response({"response": serializer.data})

    def post(self, request):
        player_data = PlayerPostSerializers(data=request.data)

        if player_data.is_valid():
            player_data.save(user=request.user)
            return Response(player_data.data)
        else:
            return Response(player_data.errors)



# class CoachView(APIView):
#     """ Coach """
#
#     def get(self, request):
#         coaches = Coach.object.filter(user=request.user)
#         serializer = CoachSerializers(coaches, data=request.data)
#         return Response({"response": serializer.data})
