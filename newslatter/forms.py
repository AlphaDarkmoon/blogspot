from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(
        label='',  # Empty label to hide it
        max_length=128,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address...'}),  # Add a placeholder
    )
