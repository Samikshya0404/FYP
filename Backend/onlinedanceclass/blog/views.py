from rest_framework import viewsets
from blog.models import Blog
from blog.serializers import BlogSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer