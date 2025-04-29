from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from store.models import Product,  Buyer, Order

@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_buyer = Buyer.objects.count()
    total_order = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    paginator = Paginator(orders, 5)
    page = request.GET.get('page')
    paged_order = paginator.get_page(page)
    context = {
        'product': total_product,
        'buyer': total_buyer,
        'order': total_order,
        'orders': paged_order
    }
    return render(request, 'dashboard.html', context)

# def dashboard_order_list(request):
#     order = Order.objects.all()
#     paginator = Paginator(order,5)
#     page = request.GET.get('page')
#     paged_dashboard = paginator.get_page(page)
#     context = {
#         'order' : paged_dashboard
#     }
#     return render(request, 'dashboard.html', context)