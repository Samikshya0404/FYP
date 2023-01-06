from rest_framework import serializers
from .models import Styles


class StylesSerializer(serializers.Serializer):
   class Meta:
      model = Styles
      fields = ['id', 'style_name']
       


