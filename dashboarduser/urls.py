from django.urls import path
from .views import *

urlpatterns = [         
    path('api/dashboardinternalpost',DashboardInternalPosts.as_view()),
    path('api/dashboardexternalpost',DashboardExternalPosts.as_view()),    
]