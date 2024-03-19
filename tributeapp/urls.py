from django.urls import path
from . import views

urlpatterns = [
    # path('route/a/', views.route_a, name='route_a'),
    # path('route/b/', views.route_b, name='route_b'),
    # path('example/', views.example_view, name='example'),
    # path('test/', views.test, name='test'),
    path('profile/<occupation>/<filename>/', views.serve_tribute_profile, name='profile'),
]

root = [path('', views.serve_root, name='root')]
