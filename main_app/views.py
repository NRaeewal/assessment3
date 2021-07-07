from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Widget

from .forms import WidgetForm


# Create your views here.

from django.http import HttpResponse

# Define the home view
def home(request):
  return render (request, 'home.html')


def add_widget(request, widget_id):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget.save()
    return redirect('home', widget_id= widget_id)


def widgets_index(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget_form = WidgetForm()
    return redirect(request, 'home.html', {
        'widget': widget, 'widget_form': widget_form
    })
