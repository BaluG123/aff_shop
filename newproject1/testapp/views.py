from django.shortcuts import render
from . models import items

# Create your views here.
def home_view(request):
    items_list=items.objects.all()
    return render(request,'testapp/home.html',{'items_list':items_list})