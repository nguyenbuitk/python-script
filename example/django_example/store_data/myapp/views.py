from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm

def job_application_view(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('job_application')
    else:
        form = ApplicationForm()
    return render(request, 'index.html', {'form': form})