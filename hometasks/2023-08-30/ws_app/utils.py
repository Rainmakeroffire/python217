from django.db.models import Q

from .models import Product, Category, Manufacturer


def search_engine(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    manufacturers = Manufacturer.objects.all()

    search_query = request.GET.get('search', '')
    selected_categories = request.GET.getlist('category')
    selected_manufacturers = request.GET.getlist('manufacturers')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    selected_ratings = request.GET.getlist('ratings')
    sort_by = request.GET.get('sort_by', '')

    if selected_categories:
        products = products.filter(categories__in=selected_categories)

    if selected_manufacturers:
        products = products.filter(manufacturer__in=selected_manufacturers)

    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(manufacturer__name__icontains=search_query))

    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)
    elif min_price:
        products = products.filter(price__gte=min_price)
    elif max_price:
        products = products.filter(price__lte=max_price)

    if selected_ratings:
        products = products.filter(rating__in=selected_ratings)

    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'rating_asc':
        products = products.order_by('rating')
    elif sort_by == 'rating_desc':
        products = products.order_by('-rating')

    context = {
        'products': products,
        'categories': categories,
        'manufacturers': manufacturers,
        'selected_categories': selected_categories,
        'selected_manufacturers': selected_manufacturers,
        'min_price': min_price,
        'max_price': max_price,
        'selected_ratings': selected_ratings,
        'sort_by': sort_by,
    }

    return context
