from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'email',
        'nama_depan',
        'nama_belakang',
        'email',
        'nomor_telephone',
        'provinsi',
        'kota',
        'kecamatan',
        'kelurahan',
        'alamat',
        'kode_pos'
    )
    list_filter = [
        'nama_depan',
        'email',
        'nomor_telephone',
        'kota',
        'kecamatan',
        'kelurahan',
        'kode_pos'
    ]

admin.site.register(Profile, ProfileAdmin)