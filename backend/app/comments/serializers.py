'''
Serializers for comments API
'''

from rest_framework import serializers
from core.models import Comments


class CommentsListSerializer(serializers.ModelSerializer):
    '''Serializer for list of comments'''

    class Meta:
        model = Comments
        fields = ['author', 'content']
