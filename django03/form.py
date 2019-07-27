from django import forms

class addNum(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    name = forms.CharField(max_length=20)