""" Forms settings and initialization """

from django import forms

from .models import Commission

class CommissionForm(forms.ModelForm):
    """
    Class to create a form based on the commission model object 
    """
    class Meta:
        model = Commission
        fields = '__all__'