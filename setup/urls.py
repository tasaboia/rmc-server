from django.contrib import admin
from django.urls import path, include
from rmc.views import UserViewSet
from rmc.views import UserViewSet, ProfessionalViewSet, SessionViewSet, CustomUserCreate
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='User')
router.register('professional', ProfessionalViewSet, basename='Professional')
router.register('session', SessionViewSet, basename='Session')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('api/user/', include('rmc.urls', namespace='rmc')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/authentication/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
