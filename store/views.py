<<<<<<< HEAD
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotAllowed
from django.contrib import messages


=======
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
>>>>>>> 1074f0aa0d82a4919a3df8e7085d78470368cdc7

from users.models import User
from .models import (
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery
)
from .forms import (
    SupplierForm,
    BuyerForm,
    SeasonForm,
    DropForm,
    ProductForm,
    OrderForm,
    DeliveryForm
)


# Supplier views
<<<<<<< HEAD

@login_required(login_url='login')
def create_supplier(request):
    if request.method == 'POST':
        print("=== POST request to create_supplier ===")
        form = SupplierForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            retype_password = form.cleaned_data['retype_password']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            
            # Check existing username
            if User.objects.filter(username=username).exists():
                print("Username already exists:", username)
                form.add_error('username', 'Username already taken.')
                return render(request, 'store/create_supplier.html', {'form': form})
            
            # Check password match
            if password != retype_password:
                print("Password mismatch")
                form.add_error('retype_password', 'Passwords do not match')
                return render(request, 'store/create_supplier.html', {'form': form})
            
            print("Creating user...")
            user = User.objects.create_user(username=username, password=password, email=email)
            print(f"User created: {user.username}, id: {user.id}")
            
            # If you have is_supplier field, uncomment; otherwise skip
            # user.is_supplier = True
            # user.save()
            
            print("Creating Supplier profile...")
            Supplier.objects.create(user=user, name=name, address=address)
            print("Supplier created – redirecting now")
            return redirect('supplier-list')
        else:
            print("Form invalid – errors:", form.errors)
    else:
        print("GET request to create_supplier")
        form = SupplierForm()
    
    return render(request, 'store/create_supplier.html', {'form': form})
=======
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(
                    username=username, password=password,
                    email=email, is_supplier=True
                )
                Supplier.objects.create(user=user, name=name, address=address)
                return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)

>>>>>>> 1074f0aa0d82a4919a3df8e7085d78470368cdc7

class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
<<<<<<< HEAD
    context_object_name = 'suppliers'   # plural for a list



# Buyer views
def create_buyer(request):
    if request.method == 'POST':
        print("=== POST request received ===")
        form = BuyerForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            retype_password = form.cleaned_data['retype_password']
            email = form.cleaned_data['email']
            
            if User.objects.filter(username=username).exists():
                print("Username already exists")
                form.add_error('username', 'Username already taken.')
                return render(request, 'store/create_buyer.html', {'form': form})
            
            if password != retype_password:
                print("Password mismatch")
                form.add_error('retype_password', 'Passwords do not match')
                return render(request, 'store/create_buyer.html', {'form': form})
            
            print("Creating user...")
            user = User.objects.create_user(username=username, password=password, email=email)
            print(f"User created: {user.username}, id: {user.id}")
            
            # Skip is_buyer for now
            # user.is_buyer = True
            # user.save()
            
            print("Creating Buyer profile...")
            Buyer.objects.create(
                user=user,
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address']
            )
            print("Buyer created – redirecting now")
            return redirect('buyer-list')
        else:
            print("Form invalid – errors:", form.errors)
    else:
        print("GET request")
        form = BuyerForm()
    return render(request, 'store/create_buyer.html', {'form': form})
class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyers'   # plural is more accurate
=======
    context_object_name = 'supplier'


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
                user = User.objects.create_user(
                    username=username, password=password,
                    email=email, is_buyer=True
                )
                Buyer.objects.create(user=user, name=name, address=address)
                return redirect('buyer-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_buyer.html', context)


class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer'
>>>>>>> 1074f0aa0d82a4919a3df8e7085d78470368cdc7


# Season views
@login_required(login_url='login')
def create_season(request):
    forms = SeasonForm()
    if request.method == 'POST':
        forms = SeasonForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('season-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_season.html', context)


class SeasonListView(ListView):
    model = Season
    template_name = 'store/season_list.html'
    context_object_name = 'season'


# Drop views
@login_required(login_url='login')
def create_drop(request):
    forms = DropForm()
    if request.method == 'POST':
        forms = DropForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('drop-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_drop.html', context)


class DropListView(ListView):
    model = Drop
    template_name = 'store/drop_list.html'
    context_object_name = 'drop'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            design = forms.cleaned_data['design']
            color = forms.cleaned_data['color']
            buyer = forms.cleaned_data['buyer']
            season = forms.cleaned_data['season']
            drop = forms.cleaned_data['drop']
            Order.objects.create(
                supplier=supplier,
                product=product,
                design=design,
                color=color,
                buyer=buyer,
                season=season,
                drop=drop,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


# Delivery views
@login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_delivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'
<<<<<<< HEAD
 
 
@login_required
def update_order_status(request, order_id):
    # Only admin (staff) can change status
    if not request.user.is_staff:
        raise PermissionDenied("You are not authorised to change order status.")
    
    # Only allow POST requests
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    order = get_object_or_404(Order, id=order_id)
    new_status = request.POST.get('status')
    valid_statuses = ['pending', 'approved', 'complete', 'decline', 'bulk']
    
    if new_status in valid_statuses:
        order.status = new_status
        order.save()
        messages.success(request, f"Order #{order.id} status updated to {new_status}.")
    else:
        messages.error(request, "Invalid status value.")
    
    return redirect('dashboard')
=======
 
>>>>>>> 1074f0aa0d82a4919a3df8e7085d78470368cdc7
