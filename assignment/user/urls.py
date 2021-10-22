from django.urls import path
from user.views import (api_register_user
                        )
urlpatterns = [
    path('/register', api_register_user, name='register'),

]
