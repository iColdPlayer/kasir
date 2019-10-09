from import_export import resources
from .models import DaftarTransaksi

class TransactionResources(resources.ModelResource):
    class Meta:
        model = DaftarTransaksi
