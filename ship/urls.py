from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('services', views.ServicesView.as_view(), name='services'),
    path('gallery', views.GalleryView.as_view(), name='gallery'),
    path('contact', (views.ContactView.as_view()), name='contact'),
    path('live-tracker', (views.TrackingView.as_view()), name='live-tracking-services'),
    # path('update-orders', (views.UpdateTracksView.as_view()), name='update-tracks'),
    path('search_track', views.search_details, name='search-details'),

]
