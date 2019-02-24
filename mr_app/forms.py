from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, ButtonHolder, Field
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
            Field('inst2', css_class='pb-5'),
            Submit('submit', 'Submit', css_class='btn-success')
        )

    class Meta:
        model = MRInput
        fields = ('sopx', 'sopy', 'r1px', 'r1py', 'r1pface', 'inst1', 'r2px', 'r2py', 'r2pface', 'inst2')
        labels = {"sopx": "Size of Plateau X", "sopy": "Size of Plateau Y", "r1px": "Rover 1 X Position", "r1py": "Rover 1 Y Position", "r1pface": "Rover 1 Facing Direction", "inst1": "Rover 1 Instruction Set", "r2px": "Rover 2 X Position", "r2py": "Rover 2 Y Position", "r2pface": "Rover 2 Facing Direction", "inst2": "Rover 2 Instruction Set"}
    