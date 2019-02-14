from django.shortcuts import render
from .models import Barang

# Create your views here.
def home(request):
    barang = Barang.objects.all()
    return render(request, 'home/home.html', {'barangs':barang})

def post_detail(request, post_id):
    barang = Barang.objects.get(pk = post_id)
    return render(request, 'home/post_detail.html', {'barangs':barang})