from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('project.urls')),
    # для работы с  дэбагом 
    # path("__debug__/", include("debug_toolbar.urls")),
]


# if settings.DEBUG:
    
#     urlpatterns += static(settings.STATIC_URL,
#                            document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL,
#                            document_root=settings.MEDIA_ROOT)
   

