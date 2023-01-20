from django import forms

from .models import User ,infodata

class UserRegistertions(forms.ModelForm):
   
    class Meta:

        model = infodata
        fields = ['name' , 'email' , 'password']
        widgets = {
        'name': forms.TextInput(attrs={'class': u'form-control' , 'id' : 'txtname'}),
        'email': forms.EmailInput(attrs={'class': u'form-control' , 'id' : 'txtemail'}),
        'password': forms.PasswordInput(attrs={'class': u'form-control' , 'id': 'txtpassword'})
    }
    #     widgets = {
    #     'name': forms.TextInput(attrs={'class': u'form-control' , 'id' : 'txtname'}),
    #     'email': forms.EmailInput(attrs={'class': u'form-control' , 'id' : 'txtemail'}),
    #     'password': forms.PasswordInput(attrs={'class': u'form-control' , 'id' : 'txtpassword'})
    # }
 