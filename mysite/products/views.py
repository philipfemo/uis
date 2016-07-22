from django.db import transaction
from django.utils import timezone
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
#from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
#from .models import Choice, Question
#from django.utils.decorators import method_decorator
from .models import Product, Category, ManageOperation, ProductStock
from .forms import ProductForm, CategoryForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.forms import modelformset_factory
# Create your views here.
#@method_decorator(login_required(login_url = "/login"), name = "dispatch")
class CreateProductView(FormView):
    template_name = "product_form.html"
    form_class = ProductForm

    def get_success_url(self):
        return reverse("products:productslist")

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        product = form.save(commit=False)
        product.author = self.request.user
        product.save()

        return super(CreateProductView, self).form_valid(form)

#@method_decorator(login_required(login_url = "/login"), name = "dispatch")
class IndexView(ListView):
    model = Product
    template_name = "productslist.html"

class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = '/products'

class CreateCategoryView(FormView):
    template_name = "category_form.html"
    form_class = CategoryForm

    def get_success_url(self):
        return reverse("products:categorieslist")

    def form_valid(self, form):
        category = form.cleaned_data["category"]
        Category.objects.create(category = category)

        return super(CreateCategoryView, self).form_valid(form)

class CategoryIndexView(ListView):
    model = Category
    template_name = "categorylist.html"

class UpdateCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = "/products/categories"

@transaction.atomic()
def manage_products(request):
    ProductFormSet = modelformset_factory(Product, fields = ("stock",), extra = 0)
    if request.method == 'POST':
        formset = ProductFormSet(request.POST, request.FILES)
        operations = ManageOperation.objects.filter(date_closed__isnull = True)
        if operations.exists():
            operation = operations[0]
            if formset.is_valid():
                formset.save()
                operation.closed_by = request.user
                operation.date_closed = timezone.now()
                operation.save()
                product_stocks = ProductStock.objects.filter(operation = operation)
                for product_stock in product_stocks:
                    product_stock.stock_closed = product_stock.product.stock
                    product_stock.save()
                return redirect('..')
            else:
                return render(request, 'manage_products.html', {'formset': formset , "products": Product.objects.all()})
        else:
            if formset.is_valid():
                products = formset.save()
                operation = ManageOperation.objects.create(opened_by = request.user)
                for product in products:
                    ProductStock.objects.create(
                        product = product,
                        operation = operation,
                        stock_opened = product.stock,
                    )
                return redirect('..')
            else:
                return render(request, 'manage_products.html', {'formset': formset , "products": Product.objects.all()})
    else:
        formset = ProductFormSet()
        return render(request, 'manage_products.html', {'formset': formset , "products": Product.objects.all()})

class OperationHistoryView(ListView):
    template_name = "history.html"
    model = ManageOperation
    context_object_name = "operations"

#def projectslist(request):
#    projects = Project.objects.all()
#    context = {
#        "objects_list": projects,
#        "title": "List"
#    }
#    return render(request, "projectslist.html", context)
