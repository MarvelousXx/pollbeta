from django.shortcuts import render
from . import models

# Create your views here.
def poll_list(req):
    polls = models.Poll.objects.all()
    return render(rer, 'poll_list.html', {'poll_list':polls})