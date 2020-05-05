
from django.conf.urls import url
from django.contrib import admin
from .views import(
    cart_home,
    cart_update
)

urlpatterns = [
    url(r'^$',cart_home,name="home"),
    #url(r'^(?P<slug>[\w-]+)/$', product_list),
    url(r'^update/$',cart_update,name='update'),
    ]
