from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.timezone import now

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='profile_picture.png', upload_to='profile_pictures')
    nama_depan = models.CharField(blank=True, max_length=20)
    nama_belakang = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=False, max_length=30)
    nomor_telephone = models.IntegerField(blank=True, null=True)
    provinsi = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=50, blank=True, null=True)
    kecamatan = models.CharField(max_length=50, blank=True, null=True)
    kelurahan = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    kode_pos = models.IntegerField(blank=True, null=True)


    joined = models.DateTimeField(default=now , editable=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)