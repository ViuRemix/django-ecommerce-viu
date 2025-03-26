from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Address


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label='Tên')
    last_name = forms.CharField(max_length=30, required=True, label='Họ')
    email = forms.EmailField(required=True, label='Email')
    dob = forms.DateField(required=False, label='Ngày sinh', widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(max_length=15, required=False, label='Điện thoại')
    gender = forms.ChoiceField(choices=[('M', 'Nam'), ('F', 'Nữ')], required=False, label='Giới tính')
    image = forms.ImageField(required=False, label='Ảnh', widget=forms.ClearableFileInput(attrs={'clear_checkbox_label': 'Xóa'}))

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email
        self.fields['gender'].choices = [('M', 'Nam'), ('F', 'Nữ')]  # Ensure choices are set

    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            super(ProfileUpdateForm, self).save(commit=commit)
        return self.instance
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'dob', 'phone', 'gender', 'image']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_name', 'street_address', 'city', 'state', 'zip_code', 'country']