from django.urls import path

from covid_spread_analyzer.prediction_app import views

urlpatterns = [
    path('prediction/', views.prediction_view, name='line_chart'),
]
