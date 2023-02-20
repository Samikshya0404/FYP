from rest_framework.serializers import ModelSerializer
from popularevents.models import PopularEvent

class PopularEventSerializer(ModelSerializer):

    class Meta:
        model = PopularEvent
        fields = "__all__"