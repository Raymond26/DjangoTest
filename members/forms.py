from django import forms
from members.models import Member

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Check', widget=forms.PasswordInput)
    location = forms.CharField(label='Location')

    class Meta:
        model = Member
        fields = ('username', 'email', 'password', 'password2', 'location')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            Member.objects.get(username=username)
        except Member.DoesNotExist:
            return username
        raise forms.ValidationError("Someone already has that username! Pick another one.")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match!")
        return password

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class AvatarUploadForm(forms.Form):
    file = forms.FileField(label='Avatar Pic')