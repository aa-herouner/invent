from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
from users.models import User
from .models import (
    Buyer,
    Category,
    Product,
    Order,
)
from .forms import (
    BuyerForm,
    CategoryForm,
    ProductForm,
    OrderForm,
)



# Buyer views
@login_required(login_url='login')
def create_buyer(request):
    forms = BuyerForm()
    if request.method == 'POST':
        forms = BuyerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(username=username, password=password, email=email, is_buyer=True)
                Buyer.objects.create(user=user, name=name, address=address)
                return redirect('buyer-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addbuyer.html', context)

class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer'


# Category views
@login_required(login_url='login')
def create_category(request):
    forms = CategoryForm()
    if request.method == 'POST':
        forms = CategoryForm(request.POST)
        if forms.is_valid():
            messages.success(request, f"{forms.cleaned_data['name']} has been added")
            forms.save()
            return redirect('category-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addCategory.html', context)


class CategoryListView(ListView):
    model = Category
    template_name = 'store/category_list.html'
    context_object_name = 'category'


# Product views
@login_required(login_url='login')
def create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            messages.success(request, f"{form.cleaned_data['name']} has been added")
            form.save()  
            return redirect('product-list') 
    context = {
        'form' : form
    }

    return render(request, 'store/addProduct.html', context)

def product_list(request):
    product = Product.objects.all()
    paginator = Paginator(product, 5)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    context = {
        'product': paged_product
    }
    return render(request, 'store/product_list.html', context)

def edit_product(request, pk):
    product_edit = get_object_or_404(Product, id=pk)
    edit_forms = ProductForm(instance=product_edit)

    if request.method == 'POST':
        edit_forms = ProductForm(request.POST, instance=product_edit)
        if edit_forms.is_valid():
            messages.success(request, f"{edit_forms.cleaned_data['name']} has been updated")
            edit_forms.save()
            return redirect('product-list')
    context = {
        'edit_forms': edit_forms
    }
    return render(request, 'store/editproduct.html', context)

# class ProductListView(ListView):
#     model = Product
#     template_name = 'store/product_list.html'
#     context_object_name = 'product'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    product = Product.objects.all()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            buyer = forms.cleaned_data['buyer']
            category = forms.cleaned_data['category']
            product = forms.cleaned_data['product']
            quantity = forms.cleaned_data['quantity']
            delivery = forms.cleaned_data['delivery']
            price = forms.cleaned_data['price']
            status = forms.cleaned_data['status']

            messages.success(request, f"{product} has been added to order")

            if product == product:
                product.quantity = product.quantity - quantity
                if product.quantity < 0:
                    # total_price = product.unit_price * product.quantity
                    # product.total_price = total_price
                    messages.error(request, f'{product.name} is out of stock')
                    return redirect('create-order')
                # elif product.quantity == 0:
                #     total_price = product.unit_price * quantity
                #     product.total_price = total_price
            product.save()

           
            Order.objects.create(
                buyer=buyer,
                category=category,
                product=product,
                quantity=quantity,
                delivery=delivery,
                price=price,
                status=status   
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addOrder.html', context)

def get_product_price(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    return JsonResponse({'unit_price': product.unit_price})

def get_order_list(request):
    order = Order.objects.all()
    paginator = Paginator(order, 5)
    page = request.GET.get('page')
    paged_order = paginator.get_page(page)
    context = {
        'order' : paged_order
    }
    return render(request, 'store/order_list.html', context)

# def dashboard_order_list(request):
#     order = Order.objects.all()
#     paginator = Paginator(order,5)
#     page = request.GET.get('page')
#     paged_dashboard = paginator.get_page(page)
#     context = {
#         'order' : paged_dashboard
#     }
#     return render(request, 'dashboard.html', context)

# class OrderListView(ListView):
#     model = Order
#     template_name = 'store/order_list.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['order'] = Order.objects.all().order_by('-id')
#         return context
    








# Delivery views
# @login_required(login_url='login')
# def create_delivery(request):
#     forms = DeliveryForm()
#     if request.method == 'POST':
#         forms = DeliveryForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('delivery-list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/addelivery.html', context)


# class DeliveryListView(ListView):
#     model = Delivery
#     template_name = 'store/delivery_list.html'
#     context_object_name = 'delivery'

# Supplier views
# @login_required(login_url='login')
# def create_supplier(request):
#     forms = SupplierForm()
#     if request.method == 'POST':
#         forms = SupplierForm(request.POST)
#         if forms.is_valid():
#             name = forms.cleaned_data['name']
#             address = forms.cleaned_data['address']
#             email = forms.cleaned_data['email']
#             username = forms.cleaned_data['username']
#             password = forms.cleaned_data['password']
#             retype_password = forms.cleaned_data['retype_password']
#             if password == retype_password:
#                 user = User.objects.create_user(username=username, password=password, email=email, is_supplier=True)
#                 Supplier.objects.create(user=user, name=name, address=address)
#                 return redirect('supplier-list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/addSupplier.html', context)


# class SupplierListView(ListView):
#     model = Supplier
#     template_name = 'store/supplier_list.html'
#     context_object_name = 'supplier'


# Season views
# @login_required(login_url='login')
# def create_season(request):
#     forms = SeasonForm()
#     if request.method == 'POST':
#         forms = SeasonForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('season-list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/addSeason.html', context)


# class SeasonListView(ListView):
#     model = Season
#     template_name = 'store/season_list.html'
#     context_object_name = 'season'


    # form = ProductForm()
    # if request.method == 'POST':
    #     form = ProductForm(request.POST)
    #     if form.is_valid():
    #         product = form.save(commit=False)
    #         product.total_price = product.quantity * product.unit_price
    #         product.save()
    #         return redirect('product-list')
    # else:
    #     form = ProductForm()    
    # context = {
    #     'form': form
    # }

    # def quantity_analysis(request):
#     product = Product.objects.all()
#     if request.method == 'POST':
#         quantity = request.POST.get(product['quantity'])
#         unit_price = request.POST.get(product['unit_price'])
#         total_price = request.POST.get(product['total_price'])
#         cal_price = quantity * unit_price
#         overall_price = cal_price == total_price
#         context = {
#             'overall_price': overall_price
#         }
#         return render(request, 'store/addProduct.html', context)
    
    # if request.method == 'POST':
    #     tp = Product.objects('total_price')
    #     t_p = tp == total_price
    #     context = {
    #         't_p': t_p
    #     }
    #     return render(request, 'store/addProduct.html', context)