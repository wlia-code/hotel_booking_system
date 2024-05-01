from django import forms
from .models import Hotel,Booking

class SearchForm(forms.Form):
    """
    Form for searching hotel rooms based on location, check-in date, check-out date, and capacity.
    """
    search_location = forms.ModelChoiceField(queryset=Hotel.objects.all(), empty_label="Select a location")
    check_in = forms.DateField(label="Check-in Date", widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField(label="Check-out Date", widget=forms.DateInput(attrs={'type': 'date'}))
    capacity = forms.IntegerField(label="Capacity")

class UserRegistrationForm(forms.Form):
    """
    Form for user registration with username and password fields.
    """
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }