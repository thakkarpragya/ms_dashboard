from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Dashboard
from .serializers import DashboardSerializer

# Create your views here.

class DashboardInternalPosts(ListCreateAPIView):      
    queryset = Dashboard.objects.filter(isInternal='Y').order_by('-postDate')         
    serializer_class = DashboardSerializer
    
class DashboardExternalPosts(ListCreateAPIView):      
    queryset = Dashboard.objects.filter(isInternal='N').order_by('-postDate')         
    serializer_class = DashboardSerializer    

#class DashboardPostDetails(RetrieveUpdateDestroyAPIView):
#    queryset = Dashboard.objects.all()
#    serializer_class = DashboardSerializer