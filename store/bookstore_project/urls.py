from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('shop.urls')),
    path('search/',include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('contact/', include('contact.urls')),
    path('order/',include('order.urls')),
    path('blog/', include('blog.urls')),
    path('vouchers/',include('vouchers.urls',namespace='vouchers')),
    path('dashboard/', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
