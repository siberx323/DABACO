from django import forms
from .models import contactclass
class contactform(forms.ModelForm):
   class Meta:
      model=contactclass
      fields =['firstname','lastname','email','msg']
      widgets={'firstname':forms.TextInput(attrs={'placeholder':'اسم'}),
               'lastname':forms.TextInput(attrs={'placeholder':'فامیل'}),
               'email':forms.TextInput(attrs={'placeholder':'ایمیل'}),
               'msg':forms.Textarea(attrs={'placeholder':'پیغام'}),
               }