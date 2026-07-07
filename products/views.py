from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    # Fetch all products from the database
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_name):
    # Fetch a single product by its name
    product = Product.objects.get(name=product_name)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        # Handle form submission to create a new product
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        # Create and save the new product
        product = Product(name=name, description=description, price=price, stock=stock)
        product.save()
        
        return redirect('product_list')  # Redirect to the product list after creation
    
    return render(request, 'product_create.html')  # Render the product creation form

def product_update(request, product_name):
    product = Product.objects.get(name=product_name)
    
    if request.method == 'POST':
        # Handle form submission to update the product
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        
        # Save the updated product
        product.save()
        
        return redirect('product_detail', product_name=product.name)  # Redirect to the product detail after update
    
    return render(request, 'product_update.html', {'product': product})  # Render the product update form

def product_delete(request, product_name):
    product = Product.objects.get(name=product_name)
    
    if request.method == 'POST':
        # Handle form submission to delete the product
        product.delete()
        return redirect('product_list')  # Redirect to the product list after deletion
    
    return render(request, 'product_delete.html', {'product': product})  # Render the product deletion confirmation page