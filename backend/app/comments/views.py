'''
Views for the comments API
'''

from rest_framework import generics

from core.models import Comments
from .serializers import CommentsListSerializer


class CommentsListView(generics.ListAPIView):
    '''Return a list of in_use comments'''
    serializer_class = CommentsListSerializer

    # redefine the queryset for retrieve only the in_use comments
    def get_queryset(self):
        return Comments.objects.filter(in_use=True)
