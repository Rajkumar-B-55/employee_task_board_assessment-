from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="TaskManager API",
        default_version='v1',
        description="API documentation for TaskManager",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),  # Allow access to all users
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', views.obtain_auth_token),
    path('api/', include('task_manager.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
