from django.contrib import admin
from cashier.models import DaftarBarang, DaftarTransaksi, ListProductTransaksi
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

admin.site.site_header = "Cashier Dashboard"
admin.site.site_title = "Cashier"
admin.site.index_title = "CPM Cashier v1.0"

class ListDaftarBarang(admin.ModelAdmin):
    search_fields = ['nama_product']
    list_display = ('nama_product', 'jumlah_produk', 'created')
    list_filter = ['user_id', 'nama_product',('created', DateRangeFilter),]

class ListProductTransaksiImport(admin.StackedInline):
    model = ListProductTransaksi

class TransactionResources(ImportExportModelAdmin):
    search_fields = ['total']
    list_display = ('produk_jumlah', 'total', 'created')
    list_filter = ['user_id', 'total',('created', DateRangeFilter),]

class ListProductTransaksiAdmin(admin.ModelAdmin):
    list_display = ('transaksi_id', 'nama_barang', 'quantity', 'subtotal', 'created')
    list_filter = ['nama_barang', ('created', DateRangeFilter)]

admin.site.register(DaftarBarang, ListDaftarBarang)
admin.site.register(DaftarTransaksi, TransactionResources)
admin.site.register(ListProductTransaksi, ListProductTransaksiAdmin)
