from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from store.models import Order, Product, Supplier, Buyer

@login_required(login_url='login')
def dashboard(request):
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_buyer = Buyer.objects.count()
    total_order = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    context = {
        'product': total_product,
        'supplier': total_supplier,
        'buyer': total_buyer,
        'order': total_order,
        'orders': orders
    }
    return render(request, 'dashboard.html', context)