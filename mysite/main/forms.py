from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = MyUsers
        fields = ['name', "password"]

    def clean_name(self):
        m_name = self.cleaned_data["name"]
        if MyUsers.objects.filter(name__iexact=m_name).count() == 0:
            raise forms.ValidationError('Такой пользователь не существует!')
        return self.cleaned_data["name"]

    def clean_password(self):
        if self.cleaned_data.get('name', None):
            m_name = self.cleaned_data["name"]
            m_password = MyUsers.objects.filter(name__iexact=m_name)
            if m_password.count() != 0:
                for m_user in m_password:
                    if m_user.password != self.cleaned_data["password"]:
                        raise forms.ValidationError('Неправильный пароль!')
        return self.cleaned_data["password"]


class RegForm(forms.ModelForm):
    class Meta:
        model = MyUsers
        fields = ['name', "password"]

    def clean_name(self):
        m_name = self.cleaned_data["name"]
        if MyUsers.objects.filter(name__iexact=m_name).count() != 0:
            raise forms.ValidationError('Такой пользователь уже существует!')
        return self.cleaned_data["name"]

    def clean_password(self):
        return self.cleaned_data["password"]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'