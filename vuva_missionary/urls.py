from django.urls import path
from vuva_missionary import views

urlpatterns = [
    path('missionary_home/', views.missionary_home, name='missionary_home'),
    path('vuva-events/', views.vuva_events, name='vuva_events'),
    path('missionary_prayer_requests/',views.missionary_prayer_requests,name='missionary_prayer_requests'),
    path('missionary_reports',views.missionary_reports,name='missionary_reports'),
]