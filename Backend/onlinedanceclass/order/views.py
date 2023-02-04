from rest_framework import viewsets
from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer