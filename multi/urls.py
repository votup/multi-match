from django.urls import path
from django.conf import settings
from django.views.generic.detail import DetailView

from . import views 

app_name = 'multi'
urlpatterns = [
  path('', views.index, name='index'),
  path('about/', views.about, name='about'),
  path('candidate_detail/(P<slug>[-\w]+)', views.CandidateDetailView, name='candidate_detail'),
    
    
]