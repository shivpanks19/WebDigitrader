from django.conf.urls import url
from . import views

from django.conf.urls import url
from stock import views as core_views

app_name = 'stock'

urlpatterns = [
    #/stock/
    url('^$',views.IndexView.as_view(), name ='index'),
    url(r'^$', views.IndexView.as_view(),name='my_function'),

    url('^(?P<pk>[0-9]+)/$',views.DetailView.as_view() , name="detail"),

    url('category/add/$',views.CategoryCreate.as_view(),name="category-add"),
    url('category/(?P<pk>[0-9]+)/$',views.CategoryUpdate.as_view(),name="category-update"),
    url('category/(?P<pk>[0-9]+)/delete/$',views.CategoryDelete.as_view(),name="category-delete"),

    url('product/add/$',views.ProductCreate.as_view(),name="product-add"),
    url('product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name="product-update"),
    url('product/(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name="product-delete"),


    url(r'^signup/$', core_views.signup, name='signup'),
]