from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super(SignupForm, self).__init__(*args, **kwargs)
    #     if self.errors:
    #         for f_name in self.fields:
    #             if f_name in self.errors:
    #                 classes = self.fields[f_name].widget.attrs.get(&#39;class&#39;, &#39;&#39;)
    #                 classes += &#39; errors&#39;
    #                 self.fields[f_name].widget.attrs[&#39;class&#39;] = classes
    #                 print(f_name)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }))

    first_name = forms.CharField(
        label='First Name',
        max_length=30,
        required=False,
        help_text='Optional.',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'first name'
        }))

    last_name = forms.CharField(
        label='Last Name',
        max_length=30,
        required=False,
        help_text='Optional.',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'last name'
        }))

    email = forms.EmailField(
        label='Email',
        max_length=255,
        help_text='Required.',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'valid email'
        }))

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }))

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password Again'
        }))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except:
            return username

        raise forms.ValidationError('username is already taken')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     return cleaned_data

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
