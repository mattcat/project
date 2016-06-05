"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from myapp import views
from accounts.views import (login_view,logout_view, register_view )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^register/', register_view, name="register"),
    url(r'^input/$', views.prono_create, name="input"),
    url(r'^teams/$', views.teams, name="teams"),
    url(r'^games/$', views.games, name="games"),
    url(r'^teams/(?P<id>\d+)/$', views.team_detail, name="team_detail"),
    url(r'^users/(?P<id>\d+)/$', views.user_detail, name="user_detail"),
    url(r'^games/(?P<id>\d+)/$', views.game_detail, name="game_detail"),
    url(r'^$', views.users, name="users"),
]
