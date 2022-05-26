from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='file', widget=forms.FileInput(attrs={'class':'form-control'}))
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)