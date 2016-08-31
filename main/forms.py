from django import forms
from django.forms import TextInput, Textarea


class ContactUs(forms.Form):
    first_name = forms.CharField(max_length=255, label="")
    last_name = forms.CharField(max_length=255, label="")
    email = forms.EmailField(max_length=255, label="")
    phone_number = forms.CharField(max_length=30, label="", required=False)
    company = forms.CharField(max_length=30, label="", required=False)
    comment = forms.CharField(widget=forms.Textarea, label="")

    def __init__(self, *args, **kwargs):
        super(ContactUs, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = TextInput(attrs={
            'class': 'text-input-grey',
            'data-validation': 'required',
            'placeholder': 'First Name*'})
        self.fields['last_name'].widget = TextInput(attrs={
            'class': 'text-input-grey',
            'data-validation': 'required',
            'placeholder': 'Last Name*'})
        self.fields['email'].widget = TextInput(attrs={
            'class': 'text-input-grey',
            'placeholder': 'Email*'})
        self.fields['phone_number'].widget = TextInput(attrs={
            'class': 'text-input-grey',
            'placeholder': 'Phone Number'})
        self.fields['company'].widget = TextInput(attrs={
            'class': 'text-input-grey',
            'placeholder': 'Company'})
        self.fields['comment'].widget = Textarea(attrs={
            'class': 'text-input-grey',
            'placeholder': 'Type your inquiry here ...'})
