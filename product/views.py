from django.shortcuts import render, HttpResponse
from product.models import Products, Category

# Create your views here.

def index(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    category_counts = []
    for category in categories:
        product_count = category.products.count()
        category_counts.append({
            'name': category.name,
            'count': product_count
        })
    print(category_counts)
    context = {
        'products': products,
        'category_counts': category_counts
    }
    return render(request, 'product/product.html', context)

def create_product(request):
    try:
        if request.method == 'POST':
            product_name = request.POST.get('product_name')
            description = request.POST.get('description')
            price = request.POST.get('price')

            # Perform any necessary processing with the form data
            product = Products(name = product_name, description= description, price = price)
            product.save()

            return HttpResponse("Success", status = 200)
        else:
            raise Exception
    except Exception as e:
        return HttpResponse(f" {e} some Error", status = 400)

        # Render a success template or redirect to another page

def create_category(request):
    try:
        if request.method == "POST":
            category_name = request.POST.get('category_name')
            product_name = request.POST.get("productObj")
            product = Products.objects.filter(name = product_name).first()
            print(category_name)
            print(product.id)
            cat = Category.objects.filter(name=category_name)
            if cat.exists():
                category = cat.first()
                category.products.add(product)
                category.save()
            else:
                # Create new category and add product to it
                category = Category.objects.create(category_name=category_name)
                category.products.add(product)
        status = 200

    except Exception as e:
        status = 400
        print(e)
    return HttpResponse("request received" , status = status)
    