from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Mpampiasa, Mpitsabo


class FandraisanaMpampiasaForm(UserCreationForm):
    anarana_feno = forms.CharField(max_length=150, required=True, label="Anarana feno")
    email = forms.EmailField(required=True, label="Email")
    no_telifonina = forms.CharField(max_length=30, required=False, label="Nomeraon-telefaona")

    class Meta:
        model = Mpampiasa
        fields = ['username', 'anarana_feno', 'email', 'no_telifonina', 'password1', 'password2']


class FidiranaMpampiasaForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


class FandraisanaMpitsaboForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = Mpitsabo
        fields = ['anarana', 'sary', 'momba', 'laharana', 'taona_asa']

    def save(self, commit=True):
        mpampiasa = Mpampiasa.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            is_mpitsabo=True
        )
        mpitsabo = super().save(commit=False)
        mpitsabo.mpampiasa = mpampiasa
        if commit:
            mpitsabo.save()
        return mpitsabo
