from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.utils import timezone

from . import models


@login_required
def home(request):
    if request.method == 'POST':
        models.Weight.objects.create(
            user=request.user,
            date=timezone.now().date(),
            weight=request.POST['weight']
        )
        return redirect(reverse('home'))
    else:
        return render(request, 'weight/home.html')
