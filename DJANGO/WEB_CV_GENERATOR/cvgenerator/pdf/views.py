from django.shortcuts import render
from pdf.models import Profile

def accept(request):
    return render(request,'pdf/accept.html')