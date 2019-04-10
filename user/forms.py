from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class createUser(UserCreationForm):
    email = forms.EmailField(help_text = False)
    def __init__(self, *args, **kwargs):
        return super(createUser,self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text={
            'username':False,
            'email':False,
            'password1':False,
            'password2':False
        }
    
class UpdateUser(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']
        help_text = {
            'username':False,
            'email':False
        }

    