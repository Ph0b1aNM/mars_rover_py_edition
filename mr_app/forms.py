from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import MRInput

class InputForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'sopx', 
            'sopy', 
            'r1px', 
            'r1py', 
            'r1pface', 
            'inst1', 
            'r2px', 
            'r2py', 
            'r2pface', 
            'inst2',
            Submit('submit', 'Submit', css_class='btn-success')
        )

    class Meta:
        model = MRInput
        fields = ('sopx', 'sopy', 'r1px', 'r1py', 'r1pface', 'inst1', 'r2px', 'r2py', 'r2pface', 'inst2')
    