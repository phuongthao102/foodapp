from django.template.context_processors import request

from .models import Store, Food, Tag,Lesson, User, Comment
from rest_framework import serializers

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store  # Đảm bảo rằng Store được định nghĩa trong food.models
        fields = '__all__'  # Hoặc liệt kê các trường cụ thể nếu cần
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)
    def get_image(self, food):

        if food.image:
            request = self.context.get('request')
            if request:
                return  request.build_absolute_uri('/static/%s' % food.image.name)
            return '/static/%s' % food.image.name
class FoodSerializer(BaseSerializer):

    class Meta:
        model = Food
        fields = '__all__'

class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password','email','avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


    def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'content','user']