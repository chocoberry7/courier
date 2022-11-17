from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q
from .models import TrackingId, PackageProgress, Summary, SendersInfo, ContactInfo, ReceiversInfo


class HomeView(View):
    def get(self, request):
        return render(request, 'main/home.html')


class ServicesView(View):
    def get(self, request):
        return render(request, 'main/services.html')


class GalleryView(View):
    def get(self, request):
        return render(request, 'main/gallery.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'main/contact.html')


class TrackingView(View):
    def get(self, request):
        return render(request, 'main/track-shipment.html')

#
# def search_details(request):
#     if request.method == "GET":
#         searched = request.GET.get('searched')
#         tracking_items = TrackingId.objects.filter(name__contains=searched)
#         tracking_contact = ContactInfo.objects.all()
#         tracking_receiver = ReceiversInfo.objects.all()
#         tracking_sender = SendersInfo.objects.all()
#         tracking_progress = PackageProgress.objects.all()
#         tracking_summary = Summary.objects.all()
#         return render(request, 'main/track.html', {'searched': searched,
#                                                    'tracking_items': tracking_items,
#                                                    'tracking_contact': tracking_contact,
#                                                    'tracking_receiver': tracking_receiver,
#                                                    'tracking_sender': tracking_sender,
#                                                    'tracking_progress': tracking_progress,
#                                                    'tracking_summary': tracking_summary})
#     else:
#         return render(request, 'main/track.html', {})


def search_details(request):
    query = request.GET.get('q', '')
    if query:
        queryset = (Q(TrackingId=query))
        # queryset = (Q(text__icontains=query))|(Q(other__icontains=query))
        results = TrackingId.objects.filter(queryset).distinct()
        return render(request, 'main/track.html', {'results': results })
    else:
        results = []
    return render(request, 'main/track.html', {'results': results, 'query': query})
