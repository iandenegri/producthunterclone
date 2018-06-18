from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.

def index(request):
    products = Product.objects
    return render(request, 'products/index.html', {'products':products})

@login_required
def create(request):
    if request.method == 'POST':
        # Trying to submit their product
        if request.POST['title'] and request.POST['description'] and request.FILES['image'] and request.FILES['icon'] and request.POST['website']:
            product=Product()
            product.title=request.POST['title']
            product.body=request.POST['description']
            product.url=request.POST['website']
            product.product_img=request.FILES['image']
            product.product_icon=request.FILES['icon']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error':'Product title and description required at a minimum.'})

    else:
        # They want to create the product
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product':product})

@login_required
def upvote(request, product_id):
    if request.method=='POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
