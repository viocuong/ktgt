from django.urls import URLPattern, path
from . import views
app_name = 'main'
urlpatterns = [
    path("",views.index,name = 'index'),
    path("home",views.home,name = 'home')
]
