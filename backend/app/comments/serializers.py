'''
Serializers for comments API
'''

from rest_framework import serializers
from core.models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    '''Serializer for list of comments'''

    class Meta:
        model = Comments
        fields = ['author', 'content']
