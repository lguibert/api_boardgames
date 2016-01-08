from django.conf.urls import url, include
from webservice.models import Boardgames
from rest_framework import routers, serializers, viewsets
from rest_framework import generics

# Serializers define the API representation.
class BoardgamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boardgames
        fields = ('id', 'name', 'sub_name', 'min_player', 'max_player', 'price', 'date_buy', 'image', 'active')


# ViewSets define the view behavior.
class BoardgameViewSet(viewsets.ModelViewSet):
    queryset = Boardgames.objects.all()
    serializer_class = BoardgamesSerializer

    def get_queryset(self):
        return Boardgames.objects.filter(active=1)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'boardgames', BoardgameViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'boardgames/add', 'webservice.views.boardgames_views.addGame'),
    url(r'boardgames/update', 'webservice.views.boardgames_views.updateGame'),
    url(r'^', include(router.urls)),
]