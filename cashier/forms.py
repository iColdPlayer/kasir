from django import forms
from django.forms import ModelForm, Textarea, TextInput, inlineformset_factory
from cashier.models import DaftarBarang, DaftarTransaksi , ListProductTransaksi
from data.models import Stock
from accounts.models import Profile


"Form Daftar Barang"
class DaftarBarangForm(forms.ModelForm):
    class Meta:
        model = DaftarBarang
        fields = '__all__'


    def save(self,commit=True):
        instance = super().save(commit=False)

        #print(self.cleaned_data)

        instance.subtotal_harga_beli = instance.jumlah_produk * instance.harga_beli_satuan
        instance.harga_jual_satuan = instance.harga_beli_satuan * instance.laba_persen / 100
        instance.harga_jual_satuan = instance.harga_jual_satuan + instance.harga_beli_satuan
        laba_persen = instance.laba_persen * instance.subtotal_harga_beli / 100
        instance.subtotal_harga_jual = laba_persen + instance.subtotal_harga_beli
        #instance.user_id = request.user
        if commit:
            instance.save()

        return instance



"Form Daftar Transaksi"
class DaftarTransaksiForm(forms.ModelForm):
    class Meta:
        model = DaftarTransaksi
        fields = '__all__'
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

class ListProductTransaksiForm(forms.ModelForm):
    class Meta:
        model = ListProductTransaksi
        fields = '__all__'


class TransaksiProductListForm(forms.Form):
    nama_barang = forms.CharField(max_length=100)
    quantity = forms.IntegerField(initial=0)
    user = forms.IntegerField()


    def save(self,transaksi):
        "get data produk"
        quantity = self.cleaned_data['quantity']

        produk = DaftarBarang.objects.get(nomor =self.cleaned_data['nama_barang'])

        if produk.jumlah_produk >=  int(quantity):
            produk.jumlah_produk = produk.jumlah_produk - int(quantity)
            "jika barang == 0"
            if produk.jumlah_produk == 0:
                produk.delete()
            else:
                produk.subtotal_harga_beli = produk.jumlah_produk * produk.harga_beli_satuan
                laba_persen = produk.laba_persen * produk.subtotal_harga_beli / 100
                produk.subtotal_harga_jual = laba_persen + produk.subtotal_harga_beli
                produk.save()
        else:
            "Transaksi Gagal"
            return False

        "hitung subototal barang"
        subtotal_produk = produk.harga_jual_satuan * int(quantity)
        produk_transaksi = ListProductTransaksi.objects.create(
            transaksi_id = transaksi,
            nama_barang = produk.nama_product,
            subtotal = subtotal_produk,
            quantity = quantity
        )
        produk_transaksi.save()

        "Transaksi Sukses"
        return produk_transaksi
