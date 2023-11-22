from django import forms


class Tech_Form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter your name','class':'forms_control'}))
    email= forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'enter your email','class':'forms_control'}))
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'enter your number','class':'forms_control'}))
    device=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter device u want','class':'forms_control'}))
    