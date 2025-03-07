'''
URLs for comments endpoints
'''

from django.urls import path

from .views import CommentsListView, CommentsCreateView

app_name = 'comments'

urlpatterns = [
    path(
        'list/',
        CommentsListView.as_view(),
        name='comments-list',
    ),
    path(
        'create/',
        CommentsCreateView.as_view(),
        name='comments-create',
    ),
]
