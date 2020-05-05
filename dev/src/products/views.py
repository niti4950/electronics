from django.http import Http404
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Category
# Create your views here.

from carts.models import Cart
from .models import Product

def product_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category = category)
    context = {
        'title': category.name,
        'products': products,
    }
    return render(request, 'product/cat.html', context)

class ProductFeaturedView(ListView):
    template_name = 'product/feature.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(ListView):
    template_name = 'product/feature-detail.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug, active=True)

        except Product.DoesNotExist:
            raise Http404("product does not exist")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("uuhhhhhh!")
        return instance



class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        print(context)
        return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request,'product/list.html',context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product does't exist")
        return instance

def product_detail_view(request, pk, *args,**kwargs):
    #instance = get_object_or_404(Product,pk = pk)
    #qs = Product.objects.filter(id = pk)
    #if qs.count() == 1:
    #    instance = qs.first()
    #else:
    #    raise Http404("Product does not exist")
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product does not exist")
    context = {
        'object':instance
    }
    return render(request,'product/detail.html',context)
