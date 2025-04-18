"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
import debug_toolbar
from django.urls.resolvers import URLResolver

admin.site.site_header = "Ecommerce Admin"
admin.site.index_title = "Admin"

urlpatterns: list[URLResolver] = [
    path('', RedirectView.as_view(url='/api/', permanent=True)), # type: ignore
    path('admin/', admin.site.urls),
    path('test/', include('test1.urls')),
    path('api/', include('market.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)  # type: ignore
    # urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
