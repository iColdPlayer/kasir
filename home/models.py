from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import Profile
from data.models import Stock
from django.utils.timezone import now

"Stock Input"
class DaftarBarang(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nomor = models.AutoField(primary_key=True)
    # nama_product = models.ForeignKey(Stock, on_delete=models.CASCADE)
    nama_product = models.CharField(max_length=40, blank=False, null=False)
    jumlah_produk = models.IntegerField()
    unit_produk = models.IntegerField(blank=True, null=True)
    harga_beli_satuan = models.DecimalField(max_digits=14, decimal_places=2)
    subtotal_harga_beli = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    laba_persen = models.IntegerField()
    harga_jual_satuan = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    subtotal_harga_jual = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)

    created = models.DateTimeField(default=now , editable=False)
    updated = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nama_product


"Daftar Transaksi"
class DaftarTransaksi(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nomor = models.AutoField(primary_key=True)
    produk_jumlah = models.PositiveIntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0)

    created = models.DateTimeField(default=now, editable=False)
    updated = models.DateTimeField(default=now, editable=False)

    def publish(self):

        self.published_date = timezone.now()

    def __str__(self):
        return str(self.nomor)


class ListProductTransaksi(models.Model):
    transaksi_id = models.ForeignKey(DaftarTransaksi, on_delete=models.CASCADE)
    nama_barang = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.PositiveIntegerField(blank=True, null=True, default=0)
    subtotal = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(default=now, editable=False)

    def publish(self):

        self.published_date = timezone.now()

    def __str__(self):
        return str(self.nama_barang)
