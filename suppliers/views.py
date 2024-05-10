from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import NetworkMemberFilter
from .models import NetworkMember
from .permissions import IsActiveEmployee
from .serializers import NetworkMemberSerializer


class NetworkMemberViewSet(viewsets.ModelViewSet):
    """
    Конечная точка API, позволяющая просматривать и редактировать пользователей сети.
    """
    queryset = NetworkMember.objects.all()
    serializer_class = NetworkMemberSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [DjangoFilterBackend]
    filter_class = NetworkMemberFilter


class NetworkMemberByLevelViewSet(viewsets.ModelViewSet):
    """
    Конечная точка API, позволяющая получить пользователей сети по иерархии.
    """
    serializer_class = NetworkMemberSerializer

    def get_queryset(self):
        level = self.request.query_params.get('level')
        if level is not None:
            return NetworkMember.objects.filter(hierarchy_level=level)
        return NetworkMember.objects.all()
