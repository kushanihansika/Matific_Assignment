from django.urls import path
from team.views import (api_get_all, api_update_team, api_create_team
                        )
urlpatterns = [
    # path('', views.index, name='index'),
    # path('/all_teams', views.GetAllTeams.as_view()),
    # path('/<slug:id>', views.TeamDetails.as_view()),
    path('create', api_create_team, name='crete'),
    path('<slug>/update', api_update_team, name='update'),
    path('/all/', api_get_all, name='all'),
]
