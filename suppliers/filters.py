import django_filters
from .models import NetworkMember


class NetworkMemberFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = NetworkMember
        fields = ['country']
