"""picey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from picey.settings import MEDIA_ROOT, MEDIA_URL
from main.views import index, discover, perma, auth, new, upload, users, u_settings, nexist, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^discover/$', discover),
    url(r'^perma/(\d+)', perma),
    url(r'^auth/$', auth),
    url(r'^new/$', new),
    url(r'^upload/$', upload),
    url(r'^users/(.+)', users),
    url(r'^settings/$', u_settings),
    url(r'^logout/$', logout),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += [
    url(r'', nexist)
]
