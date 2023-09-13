from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsAutor
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, IsAutor]     # работать можно только со своими объявлениями, кроме просмотра
    # filterset_fields = ['status',]                                # реализован в filterset_class
    filterset_class = AdvertisementFilter


    """ViewSet для объявлений."""
    def perform_create(self, serializer):                           # при создании заполняется поле user из токена
        serializer.save(creator=self.request.user)
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAutor()]
        return []
