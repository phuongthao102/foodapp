# from django.urls import path, include
# from rest_framework import routers
# from . import views
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Food API",
#         default_version='v1',
#         description="APIs for FoodApp",
#         contact=openapi.Contact(email="2251010084thao@ou.edu.vn"),
#         license=openapi.License(name="ThaoDat2025"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
# # Khởi tạo router
# router = routers.DefaultRouter()
# router.register('store', views.StoreViewSet, basename='store')
#
# urlpatterns = [
#     path('', include(router.urls)),
#     re_path(r'^swagger(?P<format>\.json|\.yaml)$',
#             schema_view.without_ui(cache_timeout=0),
#             name='schema-json'),
#     re_path(r'^swagger/$',
#             schema_view.with_ui('swagger', cache_timeout=0),
#             name='schema-swagger-ui'),
#     re_path(r'^redoc/$',
#             schema_view.with_ui('redoc', cache_timeout=0),
#             name='schema-redoc')
#     # Đảm bảo rằng router.urls được bao gồm
# ]
from django.urls import path, include, re_path  # Đảm bảo import re_path
from rest_framework import routers
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token
# Khởi tạo schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Food API",
        default_version='v1',
        description="APIs for FoodApp",
        contact=openapi.Contact(email="2251010084thao@ou.edu.vn"),
        license=openapi.License(name="ThaoDat2025"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Khởi tạo router
router = routers.DefaultRouter()
router.register('store', views.StoreViewSet, basename='store')
router.register('food', views.FoodViewSet, basename='food')
router.register('lesson', views.LessonViewSet, basename='lesson')
router.register('user', views.UserViewSet, basename='user')
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),

]
