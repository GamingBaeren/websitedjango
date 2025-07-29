from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='rust_info'),
    path('server-rules/', views.server_rules, name='rust_server_rules'),
    path('ingame-laws/', views.ingame_laws, name='rust_ingame_laws'),
]
