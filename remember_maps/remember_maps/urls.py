from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic.base import TemplateView
from django.urls import path, include

from maps import views


handler404 = 'maps.views.page_not_found'

urlpatterns = [
    path('', include('social_django.urls')),
    path('admin/', admin.site.urls),
    path(
        'about/',
        TemplateView.as_view(template_name='about.html'),
        name='about'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('add_post/', views.add_post, name='add_post'),
    path('', views.index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
