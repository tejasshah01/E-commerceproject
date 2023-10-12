from django import forms
from shipping.models import shipping

class place_order(forms.ModelForm):
    class Meta:
        Model:shipping
        fields=["state","city","pincode","Location","Shipping_address"]
        