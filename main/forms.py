from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Subject, City, UniSubject


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber',
                  'position', 'address', 'profilePic')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('bio', 'birth_date', 'phoneNumber',
                  'position', 'address', 'profilePic')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'form-control'}))


class SearchForm(forms.Form):
    level_choices = [('','Cấp học'),('gcse','THCS'),('a-level-foundation','Dự bị đại học'),('under-graduate', 'Đại học'), ('graduate', 'Thạc sĩ-Master'),
                     ('research', 'Tiến sĩ-Nghiên cứu-Trợ lý giáo sư')]
    level = forms.ChoiceField(choices=level_choices, widget=forms.Select(attrs={'class': 'form-select'}))
    subject = forms.ModelChoiceField(empty_label='Ngành bạn muốn học',queryset=Subject.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))


class AdditionalStepForm(forms.Form):
    def __init__(self, *args, request, **kwargs):
        super(AdditionalStepForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['uni_subject'] = forms.ModelChoiceField(
            empty_label='Chọn môn bạn muốn học (có thể bỏ qua)', queryset=UniSubject.objects.filter(subject__subjectName=request.session.get('subject')),required=False)
        self.fields['city'] = forms.ModelChoiceField(
            empty_label='Chọn thành phố (có thể bỏ qua)', queryset=City.objects.order_by('city_name'), required=False)
