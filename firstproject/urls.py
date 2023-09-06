from django.contrib import admin
from django.urls import include, path
from .views import pingpong, index, getdata
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', pingpong),
    path('index/', index),
    path('getdata/', getdata),
    path('todo/', include("todo.urls")),
    path('user/', include("user.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
