
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from django.db.models import Avg

from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from app.models import Player
from datetime import date, datetime

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    @action(detail=True, methods=['get'])
    def get_player_age(self, request, pk):
        player = Player.objects.get(pk=pk)
        birthDate = player.birthDate
        birthYear = birthDate.year
        currentYear = datetime.now().year
        age = currentYear - birthYear
        return Response({'age': age})

    @action(detail=False, methods=['get'])
    def get_mean_height(self, request):
        result = Player.objects.all().aggregate(Avg('height'))
        return Response(result)

    @action(detail=True, methods=['get'])
    def get_player_bmi(self, request, pk): # 127.0.0.1:8000/api/player/1/get_player_bmi
        #bmi = weight/height/height
        player = Player.objects.get(pk=pk)
        bmi = player.weight / (player.height**2)
        return Response({'bmi': bmi})

    @action(detail=False, methods=['get']) # 127.0.0.1:8000/api/player/search?matchesMin=100
    def search(self, request):
        start = int(request.GET.get('start', 0))
        end = int(request.GET.get('end', start + 10))

        ageFrom = request.GET.get('ageFrom')
        ageTo = request.GET.get('ageTo')
        matchesMin = request.GET.get('matchesMin')
        goalsMin = request.GET.get('goalsMin')

        playerList = Player.objects.all()
        today = datetime.now()
        if ageFrom:
            maxBirthDate = datetime(today.year-int(ageFrom), today.month, today.day)
            playerList = playerList.filter(birthDate__lte=maxBirthDate)

        if ageTo:
            minBirthDate = datetime(today.year+int(ageTo), today.month, today.day)
            playerList = playerList.filter(birthDate__gte=minBirthDate)

        if matchesMin:
            playerList = playerList.filter(matches__gte=matchesMin)

        if goalsMin:
            playerList = playerList.filter(goals__gte=goalsMin)
        
        playerList = playerList[start:end]
        
        data = PlayerSerializer(instance=playerList,many=True).data
        return Response(data)

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})
