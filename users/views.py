from django.shortcuts import render

from django.utils import timezone

def timezone(request):
        curent_time = timezone.now().time()
        return curent_time