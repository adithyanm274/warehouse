from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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