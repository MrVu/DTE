from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Subject, GuestCustomer


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber', 'position', 'address', 'profilePic')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber', 'position', 'address', 'profilePic')


class UniversitiesFilterForm(forms.Form):
    subjectName = forms.ModelChoiceField(empty_label='Chọn môn học', queryset=Subject.objects.all())
    levelName = forms.ChoiceField(
        choices=(('', 'Cấp học'), ('Đại học', 'Đại học'), ('Sau đại học', 'Sau đại học'), ('Thạc sĩ', 'Thạc sĩ')))
    ieltsOverall = forms.ChoiceField(choices=(
        ('', 'IELTS Overall'), (4, '4.0'), (4.5, '4.5'), (5, '5.0'), (5.5, '5.5'), (6, '6.0'), (6.5, '6.5'),
        (7, '7.0')))
    ieltsMin = forms.ChoiceField(choices=(
        ('', 'IELTS Minimum'), (4, '4.0'), (4.5, '4.5'), (5, '5.0'), (5.5, '5.5'), (6, '6.0'), (6.5, '6.5'),
        (7, '7.0')))


class GuestCustomerForm(forms.ModelForm):
    subject = forms.ModelChoiceField(empty_label='Chọn môn học', queryset=Subject.objects.all())

    class Meta:
        model = GuestCustomer
        fields = ['subject', 'guest_name', 'email', 'level', 'ielts_min', 'ielts_overall', 'phone_number']
