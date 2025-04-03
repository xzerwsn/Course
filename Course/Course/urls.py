from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import admin
from login import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'login'


urlpatterns = [

    path('admin/', admin.site.urls),
    #path('accounts/', include('login.urls')),
    path('',views.indexView,name="home"),
    path('', include('login.urls')),
    path('', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
