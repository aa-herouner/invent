from django import forms

from .models import Buyer, Category, Product, Order


# class SupplierForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'name',
#         'data-val': 'true',
#         'data-val-required': 'Please enter name',
#     }))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'address',
#         'data-val': 'true',
#         'data-val-required': 'Please enter address',
#     }))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'email',
#         'data-val': 'true',
#         'data-val-required': 'Please enter email',
#     }))
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'username',
#         'data-val': 'true',
#         'data-val-required': 'Please enter username',
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter password',
#     }))
#     retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'retype_password',
#         'data-val': 'true',
#         'data-val-required': 'Please enter retype_password',
#     }))

class BuyerForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))


# class SeasonForm(forms.ModelForm):
#     class Meta:
#         model = Season
#         fields = ['name', 'description']

#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
#             'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'})
#         }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'size', 'quantity', 'unit_price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'size': forms.TextInput(attrs={'class': 'form-control', 'id': 'size'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'id': 'quantity'}),
            'unit_price': forms.TextInput(attrs={'class': 'form-control', 'id': 'unit_price'}),
            'total_price': forms.TextInput(attrs={'class': 'form-control', 'id': 'total_price', 'readonly': 'readonly'})
            # 'sortno': forms.NumberInput(attrs={'class': 'form-control', 'id': 'sortno'})
            }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['buyer', 'category', 'product', 'quantity', 'delivery', 'unit_price', 'price', 'status']

        widgets = {
            
            'buyer': forms.Select(attrs={'class': 'form-control', 'id': 'buyer'}),
            'category': forms.Select(attrs={'class': 'form-control', 'id': 'category'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'id': 'quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'unit_price', 'readonly': 'readonly'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control', 'id': 'price', 'readonly': 'readonly'}),
            'status' : forms.Select(attrs={'class': 'form-control', 'id': 'status'}),
            'delivery': forms.RadioSelect(attrs={'id': 'delivery'})
           
        }
            # 'supplier': forms.Select(attrs={'class': 'form-control', 'id': 'supplier'}),
            # 'design': forms.TextInput(attrs={'class': 'form-control', 'id': 'design'}),
            # 'color': forms.TextInput(attrs={'class': 'form-control', 'id': 'color'}),
            # 'season': forms.Select(attrs={'class': 'form-control', 'id': 'season'}),
            # 'drop': forms.Select(attrs={'class': 'form-control', 'id': 'drop'}),

# class DeliveryForm(forms.ModelForm):
#     class Meta:
#         model = Delivery
#         fields = '__all__'

#         widgets = {
#             'order': forms.Select(attrs={'class': 'form-control', 'id': 'order'}),
#             'courier_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'courier_name'}),
#         }
