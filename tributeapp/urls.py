from django.urls import path
from . import views

urlpatterns = [
    # path('route/a/', views.route_a, name='route_a'),
    # path('route/b/', views.route_b, name='route_b'),
    # path('example/', views.example_view, name='example'),
    # path('test/', views.test, name='test'),
    path('profile/', views.profile, name='profile'),
]

root = [path('', views.root, name='root')]
