from django.conf.urls import include, url
from django.contrib import admin
from blackjack.views import site_home

urlpatterns = [
    # Examples:
    # url(r'^$', 'games.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', site_home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blackjack/', include('blackjack.urls')),
]
