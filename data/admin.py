from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stock
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

@admin.register(Stock)
class StockResources(ImportExportModelAdmin):
    list_display = ('id','name', 'price', 'created', 'updated')
    list_filter = ['name', 'price', ('created', DateRangeFilter)]
