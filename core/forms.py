from django import forms
from .models import ContactMessage
from .models import UserEmail
from .models import Product


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'phone_number', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailiniz'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon nömrənizr'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınız', 'rows': 4}),
        }

class EmailForm(forms.ModelForm):
    class Meta:
        model = UserEmail
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email.'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount_price', 'image', 'stock_quantity', 'rating']