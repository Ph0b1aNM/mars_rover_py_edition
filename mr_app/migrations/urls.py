from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mr_app/', include('mr_app.urls')),
    path('admin/', admin.site.urls),
]