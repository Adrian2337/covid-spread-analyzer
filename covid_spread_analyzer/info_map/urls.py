from django.urls import path

from covid_spread_analyzer.info_map import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('statistics/<str:voivode>/', views.statistics_view, name='statistics'),
]
