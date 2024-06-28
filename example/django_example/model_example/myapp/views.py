from django.shortcuts import render
from .models import Person
# Create your views here.

def person_list_view(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})
