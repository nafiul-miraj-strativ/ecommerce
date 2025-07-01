from rest_framework import serializers
from apps.user.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'role')
        read_only_fields = ('role',)
    
    def create(self,validated_data):
        user = User(
            username=validated_data['username'],
            role=User.CUSTOMER
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            role=User.MANAGER
        )
        user.set_password(validated_data['password'])
        user.save()
        return user