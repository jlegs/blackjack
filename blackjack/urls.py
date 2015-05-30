from django.conf.urls import include, url
from django.contrib import admin
from blackjack.views import new_game

urlpatterns = [
    # Examples:
    # url(r'^$', 'games.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', new_game, name='new_game'),
]
