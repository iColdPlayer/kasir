from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from accounts import views as account_views
from django.views.generic.base import RedirectView


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')), #JET
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), #JET Dashboard
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('cashier.urls')),
    path('register/', account_views.Register, name='Register'),
    path('accounts/', account_views.Account, name='Account'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='Logout'),
    path('auth/', include('api.urls')),
    path('auth/', RedirectView.as_view(url='/auth/api'), name='/auth/api/'),
    path('api/', RedirectView.as_view(url='/auth/api'), name='/auth/api/'),
    path('debug/', trigger_error),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

