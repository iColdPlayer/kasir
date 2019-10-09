# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from home.models import DaftarBarang
# from home.models import DaftarTransaksi
#
#
# @receiver(post_save, sender=DaftarTransaksi)
# def update_stock(sender, instance, **kwargs):
#     instance.jumlah_produk -= instance.jumlah_produk - instance.produk_jumlah
#     instance.jumlah_produk.save()
#
