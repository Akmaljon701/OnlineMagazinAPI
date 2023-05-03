from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Online Do'kon API",
      default_version='v1',
      description="Online Do'kon uchun API",
      contact=openapi.Contact("Akmaljon Yoqubov <akmaljonyoqubov088@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/', include('asosiy.urls')),
    path('user/', include('userapp.urls')),
    path('buyurtma/', include('buyurtma.urls')),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]
