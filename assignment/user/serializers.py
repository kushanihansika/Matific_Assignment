from rest_framework import fields, serializers
from team.models import Team
from role.models import Role
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    team = serializers.CharField
    role = serializers.CharField

    class Meta:
        model = User
        fields = ['id',
                  'user_name',
                  'password',
                  'team',
                  'role']

        extra_kwargs = {
            'password': {'write_only': True}
        }
