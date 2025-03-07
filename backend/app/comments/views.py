'''
Views for the comments API
'''

from rest_framework import generics

from core.models import Comments
from .serializers import CommentsSerializer


class CommentsListView(generics.ListAPIView):
    '''Return a list of in_use comments'''
    serializer_class = CommentsSerializer

    # redefine the queryset for retrieve only the in_use comments
    def get_queryset(self):
        return Comments.objects.filter(in_use=True)


class CommentsCreateView(generics.CreateAPIView):
    '''Users can create comments'''
    serializer_class = CommentsSerializer
