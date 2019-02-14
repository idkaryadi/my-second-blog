from django.db import models

# Create your models here.
class Barang(models.Model):
    nama_barang = models.CharField(max_length = 255)
    images = models.CharField(max_length = 255)
    harga = models.CharField(max_length = 50)
    diskripsi_produk = models.TextField()
    
    def __str__(self):
        return self.nama_barang