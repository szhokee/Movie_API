from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title = 'Movie API',
        default_version = 'v1',
        description = 'Web-Site'
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('account/', include('account.urls')),
    path('feedback/', include('feedback.urls')),
    path('movies/', include('movies.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
