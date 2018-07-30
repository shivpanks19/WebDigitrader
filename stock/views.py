from django.shortcuts import render
from django.views import generic
from django.views.generic.base import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Category,Product
from django.urls import reverse_lazy
# Create your views here
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

class IndexView(generic.ListView):
    template_name = 'stock/index.html'
    context_object_name ='Category'
    def get_queryset(self):
        return Category.objects.all()


class DetailView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'stock/detail.html'


class CategoryCreate(CreateView):
    model = Category
    fields = ['cat_name','cat_id','cat_stock','cat_logo']


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['cat_name','cat_id','cat_stock','cat_logo']


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('stock:index')

class ProductCreate(CreateView):
    model = Product
    fields = ['pr_name','pr_id','pr_image','pr_category','pr_price','pr_stock','pr_mfg','pr_avb']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['pr_name', 'pr_id', 'pr_image', 'pr_category', 'pr_price', 'pr_stock', 'pr_mfg', 'pr_avb']


class ProductDelete(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse_lazy('stock:detail' ,kwargs={'pk':self.get_object().pr_category.id})





def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('stock:my_function')
    else:
        form = UserCreationForm()
    return render(request, 'stock/signup.html', {'form': form})

def my_function(request, backend):
   data = request.GET