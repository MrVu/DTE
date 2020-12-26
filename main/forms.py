from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Subject

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber', 'position', 'address', 'profilePic')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber', 'position', 'address', 'profilePic')

class UniversitiesFilterForm(forms.Form):
    subjectName = forms.ModelChoiceField(empty_label='Chọn môn học',queryset=Subject.objects.all())
    levelName = forms.ChoiceField(choices=(('','Cấp học'),('DH', 'Đại học'),('SDH', 'Sau đại học'),('TS', 'Thạc sĩ')))
    ieltsOverall = forms.ChoiceField(choices=(('','IELTS Overall'),(4,'4.0'),(4.5, '4.5'),(5,'5.0'),(5.5,'5.5'),(6,'6.0'),(6.5,'6.5'),(7,'7.0')))
    ieltsMin = forms.ChoiceField(choices=(('','IELTS Minimum'),(4,'4.0'),(4.5, '4.5'),(5,'5.0'),(5.5,'5.5'),(6,'6.0'),(6.5,'6.5'),(7,'7.0')))
