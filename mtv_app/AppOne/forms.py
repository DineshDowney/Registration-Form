from django import forms
from AppOne.models import Roll_Number,AccessRec

class FormClass2(forms.ModelForm):
    class Meta():
        model=AccessRec
        fields=("Name","message",)

class FormClass1(forms.ModelForm):
    class Meta():
        model=Roll_Number
        fields=("Roll_Num",)

