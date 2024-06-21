from django.urls import URLPattern, path

from produtos import views

urlpatterns = [
    path('', views.home, name='home'),
    path('layout-static/', views.layout_static, name='layout_static'),
]
