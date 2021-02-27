from django.urls import path, include
from .views import profile_detail_view, profile_update_view


urlpatterns = [
    path('<str:username>', profile_detail_view),
    path('update/', profile_update_view),
    path('api/', include('profiles.api.urls')),

]
