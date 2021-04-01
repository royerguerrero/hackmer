"""hackmer URL Configuration"""

# Django
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# Views
from hackmer import views
from products import views as products_views
from orders import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('datos/', views.DataHandling.as_view(), name='data'),
    path('cookies/', views.Cookies.as_view(), name='cookies'),
    path('devoluciones/', views.ReturnProducts.as_view(), name='returns'),
    path('categoria/<slug:slug>/', products_views.CategoryDetail.as_view(), name='category'),
    path('productos/', include(('products.urls', 'products'), namespace='products')),
    path('pago/', order_views.PurchaseView.as_view(), name='purchase')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
