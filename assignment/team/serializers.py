from rest_framework import fields, serializers
from .models import Team
from user.models import User
from role.models import Role


class TeamSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "team_name",
            "users"
        )
