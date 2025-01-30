# from django.core.serializers import serialize
# from rest_framework import viewsets, generics,status,parsers
# from rest_framework.response import Response
# from .serializers import FoodSerializer, LessonSerializer
# from .models import Store, Food, Lesson,User
# # from .serializers import StoreSerializer
# from . import serializers, paginators
# from rest_framework.decorators import action
#
# class StoreViewSet(viewsets.ViewSet, generics.ListAPIView):
#     queryset = Store.objects.all()
#     serializer_class = serializers.StoreSerializer
#
#     def get_queryset(self):
#         queryset = Store.objects.all()  # Thay Food bằng Store
#         q = self.request.query_params.get("q")
#         if q:
#             queryset = queryset.filter(name__icontains=q)  # Thay 'subject' bằng 'name' hoặc trường phù hợp
#         return queryset
#
# class FoodViewSet(viewsets.ViewSet, generics.ListAPIView):
#     queryset = Food.objects.filter(active=True).all()
#     serializer_class = serializers.FoodSerializer
#     pagination_class = paginators.FoodPaginator
#
#     def get_queryset(self):
#         queryset = Food.objects.all()
#         q = self.request.query_params.get("q")
#         if q:
#             queryset = queryset.filter(subject__icontains=q)
#         return queryset
#
#     @action(methods=['get'], detail=True)
#     def get_lessons(self, request, pk):
#         food = self.get_object()
#         lessons = self.get_object().lesson_set.filter(active=True).all()
#         serializer = LessonSerializer(lessons, many=True)
#         return Response(serializers.LessonSerializer(lessons, many=True, context={'request': request}).data, status=status.HTTP_200_OK)
#
#
#
# class  LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
#     queryset = Lesson.objects.filter(active=True).all()
#     serializer_class = serializers.LessonSerializer
#
# class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
#     queryset = User.objects.filter(is_active=True).all()
#     serializer_class = serializers.UserSerializer
#     pagination_class = [parsers.MultiPartParser]

#
# from django.core.serializers import serialize
# from rest_framework import viewsets, generics, status, parsers
# from rest_framework.response import Response
# from .serializers import FoodSerializer, LessonSerializer
# from .models import Store, Food, Lesson, User
# from . import serializers, paginators
# from rest_framework.decorators import action
# from rest_framework import permissions
#
# class StoreViewSet(viewsets.ModelViewSet):
#     queryset = Store.objects.all()
#     serializer_class = serializers.StoreSerializer
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         q = self.request.query_params.get("q")
#         if q:
#             queryset = queryset.filter(name__icontains=q)
#         return queryset
#
# class FoodViewSet(viewsets.ModelViewSet):
#     queryset = Food.objects.filter(active=True)
#     serializer_class = serializers.FoodSerializer
#     pagination_class = paginators.FoodPaginator
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         q = self.request.query_params.get("q")
#         if q:
#             queryset = queryset.filter(subject__icontains=q)
#         return queryset
#
#     @action(methods=['get'], detail=False)
#     def get_lessons(self, request, pk=None):
#         try:
#             food = self.get_object()
#             lessons = food.lesson_set.filter(active=True)
#             serializer = LessonSerializer(lessons, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Food.DoesNotExist:
#             return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
#
# class LessonViewSet(viewsets.ModelViewSet):
#     queryset = Lesson.objects.filter(active=True)
#     serializer_class = serializers.LessonSerializer
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(is_active=True)
#     serializer_class = serializers.UserSerializer
#     parser_classes = [parsers.MultiPartParser]
#
#
#     def get_permissions(self):
#         if self.action.__eq__('current_user'):
#             return [permissions.IsAuthenticated()]
#         return [permissions.AllowAny]
#
#
#
#
#     @action(methods=['get'], url_name='currnent-user')
#     def current_user(self, user):
#         return Response(serializers.UserSerializer(request.user).data)
from django.core.serializers import serialize
from rest_framework import viewsets, generics, status, parsers, permissions
from rest_framework.response import Response
from .serializers import FoodSerializer, LessonSerializer
from .models import Store, Food, Lesson, User, Comment
from . import serializers, paginators
from rest_framework.decorators import action

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = serializers.StoreSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.query_params.get("q")
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(active=True)
    serializer_class = serializers.FoodSerializer
    pagination_class = paginators.FoodPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.query_params.get("q")
        if q:
            queryset = queryset.filter(subject__icontains=q)
        return queryset

    @action(methods=['get'], detail=False)
    def get_lessons(self, request):
        food_id = request.query_params.get('food_id')
        try:
            food = Food.objects.get(id=food_id)
            lessons = food.lesson_set.filter(active=True)
            serializer = LessonSerializer(lessons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Food.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = serializers.LessonSerializer
    permission_classes = [permissions.IsAuthenticated()]

    def get_permissions(self):
        if self.action in ['add_comment']:
            return [permissions.IsAuthenticated()]
        return self.permission_classes

    @action(methods=['post'],url_path='comments', detail=True)
    def add_comment(self, request, pk):
        c = Comment.objects.create(user=request.user, lesson=self.get_object(), content=request.data.get('content'))

        return Response(serializers.CommentSerializer(c).data, status=status.HTTP_200_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action == 'current_user':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny]

    @action(methods=['get'], detail=False, url_name='current-user')
    def current_user(self, request):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(is_active=True)
#     serializer_class = serializers.UserSerializer
#     parser_classes = [parsers.MultiPartParser]
#
#     def get_permissions(self):
#         if self.action == 'current_user':
#             return [permissions.IsAuthenticated()]
#         return [permissions.AllowAny()]
#
#     @action(methods=['get'], detail=False, url_name='current-user')
#     def current_user(self, request):
#         serializer = serializers.UserSerializer(request.user)
#         return Response(serializer.data)