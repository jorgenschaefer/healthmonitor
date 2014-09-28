from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.utils import timezone

from . import models


@login_required
def home(request):
    if request.method == 'POST':
        weight, created = models.Weight.objects.get_or_create(
            user=request.user,
            date=timezone.now().date(),
            defaults={"weight": request.POST['weight']}
        )
        if not created:
            weight.weight = request.POST['weight']
            weight.save()
        return redirect(reverse('home'))
    else:
        weight_list = models.Weight.objects.all()
        return render(request, 'weight/home.html',
                      {"weight_list": weight_list})
