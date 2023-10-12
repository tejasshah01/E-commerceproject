from django import forms

class ship_form(forms.Form):
    state=forms.CharField(max_length=50,widget=forms.TextInput)
    city=forms.CharField(max_length=50,widget=forms.TextInput)
    pincode=forms.IntegerField(widget=forms.TextInput)
    Location=forms.CharField(max_length=50,widget=forms.TextInput)
    Shipping_address=forms.CharField(max_length=100,widget=forms.TextInput)




