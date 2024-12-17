from django.contrib import admin
from django.urls import path, include  # Import include to reference app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(('myapp.urls', 'myapp'), namespace='myapp')),  # Include myapp URLs
] 