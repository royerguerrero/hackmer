"""hackmer URL Configuration"""

# Django
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

# Views
from hackmer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('datos/', views.DataHandling.as_view(), name='data'),
    path('cookies/', views.Cookies.as_view(), name='cookies'),
    path('devoluciones/', views.ReturnProducts.as_view(), name="returns"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
