from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from allauth.account.views import SignupView

urlpatterns = [
    path('', views.home, name='home-page'),
    path('search-results/', views.search_results, name='search-results'),
    path('rooms/<int:room_id>/', views.room_detail, name='room-detail'), # Placeholder for room detail
    # ... add URLs for booking views later
]
