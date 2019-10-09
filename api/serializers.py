from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Profile

class ApiSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = (
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

class UserSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedModelSerializer()