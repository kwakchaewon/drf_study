from rest_framework import serializers
from .models import User, Board, BoardCategories, BoardReplies, BoardLikes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id','password', 'last_login', 'is_superuser', 'username', 'email', 'is_staff', 'is_active', 'date_joined', 'birth', 'phone']
        fields = ['username', 'password' ,'birth', 'email', 'phone']

        
        # extra_kwargs: 필드에 대해 다양한 옵션을 설정
        # write_only, read_only, required, allow_null 등
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
