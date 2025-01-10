'''
URL Mappings for the user API
'''
from django.urls import path
from user import views

# define the name app in the general routes file
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    # path('me/', views.ManageUserView.as_view(), name='me'),
]
