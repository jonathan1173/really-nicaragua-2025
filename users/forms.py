from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'name', 'last_name']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya existe")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está en uso")
        return email

    def clean(self):
        cleaned_data = super().clean()
        for field in self.Meta.fields:
            value = cleaned_data.get(field)
            if value in [None, '']:
                self.add_error(field, f'El campo {field} no puede estar vacío.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
