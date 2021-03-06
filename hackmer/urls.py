"""Hackmer URL Configuration"""

# Django
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

# Views
from hackmer import sitemaps, views
from products import views as products_views
from orders import views as order_views

# Sitemaps 
from hackmer import sitemaps

app_name = 'Hackmer Store'

sitemaps = {
     'static': sitemaps.StaticViewSitemap,
     'productos': sitemaps.ProductSitemap,
     'category': sitemaps.CategorySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='home'),
    path('datos/', views.DataHandling.as_view(), name='data'),
    path('cookies/', views.Cookies.as_view(), name='cookies'),
    path('devoluciones/', views.ReturnProducts.as_view(), name='returns'),
    path('categoria/<slug:slug>/', products_views.CategoryDetail.as_view(), name='category'),
    path('productos/', include(('products.urls', 'products'), namespace='products')),
    path('pago/', order_views.Purchase.as_view(), name='purchase'),
    path('pasarela/<uuid:pk>/', order_views.Payment.as_view(), name='payment'),
    path('order/<uuid:pk>/', order_views.OrderStatus.as_view(), name='order_details'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
