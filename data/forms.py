from django import forms


class UploadExcelFileForm(forms.Form):
    file = forms.FileField()


