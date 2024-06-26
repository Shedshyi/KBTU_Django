from django.shortcuts import render
from django.http import HttpResponse

from core.forms import EventForm, StudentForm, OrganizerForm


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index.html', {'form': given_form(), 'given_url': given_url})


def add_event(request):
    return add_model(request, EventForm, 'add_event', 'event')


def add_student(request):
    return add_model(request, StudentForm, 'add_student', 'student')


def add_organizer(request):
    return add_model(request, OrganizerForm, 'add_organizer', 'organizer')


# Create Views with Forms
# 1) Create a simple django view function
# 2) Create django form
# 3) Create django template
# 4) Save instances