from django.shortcuts import render
from .resources import StockResource
from tablib import Dataset

def StockUpload(request):
    if request.method == 'POST':
        stock_resource = StockResource()
        dataset = Dataset()
        new_stock = request.FILES['file']

        new_stock.seek(0)
        imported_data = dataset.load(new_stock.read())
        imported_data.save()
        result = stock_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            stock_resource.import_data(dataset, dry_run=False)

    return render(request, 'upload.html')