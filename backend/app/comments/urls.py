'''
URLs for comments endpoints
'''

from django.urls import path

from .views import CommentsListView

app_name = 'comments'

urlpatterns = [
    path(
        'list/',
        CommentsListView.as_view(),
        name='comments',
    ),
]
