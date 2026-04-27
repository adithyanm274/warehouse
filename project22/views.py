from django.shortcuts import render
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from store.models import Order, Product, Supplier, Buyer

@login_required(login_url='login')
def dashboard(request):
    context = {
        'order': Order.objects.count(),           # total orders (singular 'order')
        'product': Product.objects.count(),       # total products
        'supplier': Supplier.objects.count(),     # total suppliers
        'buyer': Buyer.objects.count(),           # total buyers
        'orders': Order.objects.select_related(
            'supplier', 'product', 'buyer', 'season', 'drop'
        ).order_by('-created_date')[:20],         # recent orders for the table
    }
    return render(request, 'dashboard.html', context)
=======

from store.models import Product, Supplier, Buyer, Order


@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_oder = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    context = {
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_oder,
        'orders': orders
    }
    return render(request, 'dashboard.html', context)
>>>>>>> 1074f0aa0d82a4919a3df8e7085d78470368cdc7
