from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from . import models

from .models import Note


# Create views here.


class HomeView(generic.View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def update_location(request):
    try:
        print(request.POST.get('point', ''))
        user_profle = models.Profile.objects.get(user=request.user)
        if not user_profle:
            raise ValueError("Can't get User details")
        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        point = Point(point, srid=4326)
        user_profle.location = point
        user_profle.save()
        return JsonResponse({"message": f"Set location to {point.wkt}."}, status=200)
    except Exception as e:
        raise e;
        # return JsonResponse({"message": JSON.stringify(e)},status=400)


def note(request):
    if request.method == 'POST':
        print(request.POST.get('note_heading'))
        note_heading = request.POST.get('note_heading')
        note_des = request.POST.get('note_des')  # Changed to 'note_des' as per your form's textarea name
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        notes = Note(note_heading=note_heading, note=note_des, lat=lat, lng=lng)

        notes.save()

        return render(request, 'home.html')

    # If it's not POST, just render the form
    return render(request, 'home.html')
