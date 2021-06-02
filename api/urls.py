from django.urls import reverse,path,URLPattern
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
app_name='api'
urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register',views.Register.as_view(),name='register'),
    path('musics',views.Musics.as_view(),name ='musics'),
    path('singer',views.singer,name='singer'),
    path('singers',views.Singers.as_view(),name='singers'),
    path('musicbysinger',views.MusicBySinger.as_view(),name='musicbysinger'),
    path('search',views.Search.as_view(),name='saerch')
]
