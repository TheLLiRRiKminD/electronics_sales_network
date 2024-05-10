from rest_framework.routers import DefaultRouter
from suppliers.apps import SuppliersConfig
from suppliers.views import NetworkMemberViewSet, NetworkMemberByLevelViewSet

app_name = SuppliersConfig.name

router = DefaultRouter()
router.register(r'', NetworkMemberViewSet, basename='Suppliers')  # Регистрация представления NetworkMemberViewSet
router.register('network_members_by_level', NetworkMemberByLevelViewSet,
                basename='NMbL')  # Регистрация представления NetworkMemberByLevelViewSet

urlpatterns = router.urls
