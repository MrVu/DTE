from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Subject, GuestCustomer, City, UniSubject


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


class GuestCustomerForm(forms.ModelForm):
    subject = forms.ModelChoiceField(
        empty_label='Chọn môn học', queryset=Subject.objects.order_by('subjectName'))

    class Meta:
        model = GuestCustomer
        fields = ['subject', 'level',
                  'guest_name', 'email', 'phone_number']


class AdditionalStepForm(forms.Form):
    def __init__(self, *args, request, **kwargs):
        super(AdditionalStepForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['uni_subject'] = forms.ModelChoiceField(
            empty_label='Chọn môn bạn muốn học (có thể bỏ qua)', queryset=UniSubject.objects.filter(subject__subjectName=request.session.get('subject')),required=False)
        self.fields['city'] = forms.ModelChoiceField(
            empty_label='Chọn thành phố (có thể bỏ qua)', queryset=City.objects.order_by('city_name'), required=False)
