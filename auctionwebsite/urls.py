from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static # < this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user_app.urls',namespace='users')),
    # path('accounts/', include('user_app.urls',namespace='accounts')),
    path('',include('goods_app.urls',namespace='goods')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # < this
