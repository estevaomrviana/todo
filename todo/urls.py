from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, PasswordChangeView, logout_then_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/logout/', logout_then_login, name='logout'),
    path(
        'change-password/',
        PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)