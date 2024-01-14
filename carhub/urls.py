from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('brand/<slug:brand_slug>', views.home, name='brand_wise_car'),

    path('singUp/', views.SignUpView.as_view(), name='signUp'),
    path('signIn/', views.SignInView.as_view(), name='singIn'),
    path('singOut/', LogoutView.as_view(), name='singOut'),

    path('car/', include('car.urls'), name='car'),
    path('brand/', include('brand.urls'), name='brand'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)