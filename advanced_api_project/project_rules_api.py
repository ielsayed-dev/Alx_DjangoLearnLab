from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Main admin interface
    path('admin/', admin.site.urls),
    
    # Step 6: Include the API application URLs
    path('api/v1/', include('api.urls')),
]