from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from tweets.views import home_view
from django.views.generic import TemplateView

from tweets.views import (
    tweets_detail_view, 
    tweets_list_view, 
    tweets_profile_view
    )

from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('profile/', include('profiles.urls')),
    path('', include('tweets.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
