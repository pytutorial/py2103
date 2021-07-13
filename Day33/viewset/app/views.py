
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from app.models import Player

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})
