from django.shortcuts import render, redirect, reverse, render_to_response
from decimal import Decimal
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import formset_factory, modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import (
    DaftarBarang,
    DaftarTransaksi,
    ListProductTransaksi,

)
from accounts.models import Profile
from cashier.forms import (
    DaftarBarangForm,
    TransaksiProductListForm,
    ListProductTransaksiForm,
    DaftarTransaksiForm,
)
from django.utils.timezone import datetime
from data.models import Stock


def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

@login_required()
def HomeIndex(request):
    today = datetime.today()
    data = DaftarBarang.objects.filter(user_id = request.user.id)
    data_pendapatan = DaftarTransaksi.objects.filter(created__day=today.day,user_id=request.user.id)
    pendapatan_hari_ini = 0
    if data_pendapatan is not None :
        for pendapatan in data_pendapatan:
            pendapatan_hari_ini += Decimal(pendapatan.total)
    #         # raise ValueError(data_pendapatan)
    context = {
        'data': data,
        'data_pendapatan': pendapatan_hari_ini
    }
    return render(request, 'cashier/home.html', context)

@login_required()
def InputStock(request):
    # if request.is_ajax():
    #     return render(request, 'input.html', { 'num': 2})
    DaftarBarangFormset = formset_factory(DaftarBarangForm , extra=1)
    formset = DaftarBarangFormset()
    stocks = Stock.objects.all()
    if request.method == 'POST':
        # return HttpResponse('tes')
        formset_post = DaftarBarangFormset(request.POST)
        if formset_post.is_valid():
            for form in formset_post:
                if form.cleaned_data['jumlah_produk'] < 1 or form.cleaned_data['harga_beli_satuan'] < 1 or form.cleaned_data['laba_persen'] < 1:
                    messages.warning(request, 'Anda belum memasukkan data dengan lengkap!.')
                    return redirect('/input/')
                form.save()
            messages.success(request, 'Barang berhasil disimpan ke dalam stock!')
            return HttpResponseRedirect('/input/')
        else:
            messages.warning(request, 'Anda belum memasukkan data dengan benar!')
            return redirect('/input/')
    else:
        context = {
            'stocks': stocks,
            'forms': formset,
            'request_user': request.user.id,
        }
        return render(request, 'cashier/input_data.html', context)


@login_required()
def TotalStock(request):
    data = DaftarBarang.objects.filter(user_id=request.user.id)
    context = {
        'data':data
    }
    return render_to_response('cashier/stock.html', context)


@login_required()
def Cart(request):
    TransaksiListProdukFormset = formset_factory(TransaksiProductListForm , extra=1)
    formset = TransaksiListProdukFormset()
    data = DaftarBarang.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        formset_post = TransaksiListProdukFormset(request.POST)
        if formset_post.is_valid():
            total_harga_transaksi = 0
            total_jumlah_transaksi = 0
            transaksi = DaftarTransaksi.objects.create(user_id=request.user.id)
            transaksi.save()
            for form in formset_post:
                #print(form.cleaned_data)
                "if quantity == 0"
                if form.cleaned_data['quantity'] < 1:
                    messages.warning(request, 'Jumlah barang yang dibeli tidak boleh kosong!')
                    return redirect('/cart/')
                output = form.save(transaksi)
                "False == Transaksi Gagal"
                if(output == False):
                    messages.warning(request, 'Barang melebihi batas stock!')
                    return redirect('/cart/')

                "Hitung Total Harga Transaksi"
                total_harga_transaksi += output.quantity
                "Hitung Total Jumlah Transaksi"
                total_jumlah_transaksi += output.subtotal
            "Update Total Ke DaftarTransaksi"
            transaksi.total = total_jumlah_transaksi
            transaksi.produk_jumlah = total_harga_transaksi
            transaksi.save()
            "True == Transaksi Sukses"
            messages.success(request, 'Transaksi Berhasil!')
            return HttpResponseRedirect('/struck/'+str(transaksi.nomor)+'/')
        else:
            messages.warning(request, 'Data yang dibeli tidak boleh kosong!')
            return redirect('/cart/')
    else:
        context = {
            'data_barang': data,
            'forms': formset,
            'request_user': request.user.id,
        }
        return render(request, 'cashier/cart.html', context)

@login_required()
def StruckPembelian(request, pk):
    dataStruck = DaftarTransaksi.objects.get(nomor=pk)
    dataStruckListProduk = ListProductTransaksi.objects.filter(transaksi_id=dataStruck.nomor)
    dataUser = Profile.objects.get(id=dataStruck.user_id)
    context = {
        'dataStruck': dataStruck,
        'dataStruckListProduk': dataStruckListProduk,
        'dataUser': dataUser
    }
    return render(request, 'cashier/struck.html', context)

@login_required()
def DaftarPembelian(request):
    data = DaftarTransaksi.objects.filter(user_id=request.user.id)
    context = {
        'data': data,
    }
    return render(request, 'cashier/purchased.html', context)


@login_required()
def ReportView(request):
    if request.is_ajax():
        endDate = None
        startDate = request.GET.get('startDate')
        if request.GET.get('endDate') == '' or request.GET.get('endDate') is None :
            endDateConverter = datetime.today()
        else:
            endDate = request.GET.get('endDate')
            endDateConverter = datetime.strptime(endDate, "%Y-%m-%d").date()
        startDateConverter = datetime.strptime(startDate, "%Y-%m-%d").date()
        from_user = DaftarTransaksi.objects.filter(user_id=request.user.id,
                                                   created__date__gte=startDateConverter,
                                                   created__date__lte = endDateConverter)
        daftar_barang = ListProductTransaksi.objects.filter(transaksi_id__in=from_user)
        return render(request, 'report_details.html', {'daftar_barang': daftar_barang, 'num': startDateConverter})
    from_user = DaftarTransaksi.objects.filter(user_id=request.user.id)
    daftar_barang = ListProductTransaksi.objects.filter(transaksi_id__in=from_user)


    context = {
        'daftar_barang': daftar_barang,
        'from_user': from_user,

    }
    return render(request, 'cashier/report.html', context)
