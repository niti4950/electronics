

from django.conf.urls import url
from django.contrib import admin
from products.views import(
                ProductListView,
                ProductDetailSlugView,
                product_list,
                product_detail_view

)

urlpatterns = [
    url(r'^$', ProductListView.as_view(),name="list"),
    #url(r'^(?P<slug>[\w-]+)/$', product_list),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(),name='detail'),
    ]
