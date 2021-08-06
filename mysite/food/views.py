from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from . import services

def login_required_decorator(func):
    return login_required(func, login_url="login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("admin_page")

    return render(request, "dashboard/login.html")

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required_decorator
def admin_page(request):
    return render(request, "dashboard/index.html")


def home_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    orders = []
    orders_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price")
    if orders_list:
        for key, val in json.loads(orders_list).items():
            orders.append(
                {
                    "product": Product.objects.get(pk=int(key)),
                    "count": val
                }
            )
    ctx = {
        "products": products,
        "categories": categories,
        "orders": orders,
        'total_price': total_price,
    }
    response = render(request, "food/index.html", ctx)
    # response.set_cookie("hello", "hello world!")
    return response

def get_data(request):
    if request.GET:
        product_id = request.GET.get("product_id")
        product = services.get_product_by_id(product_id)
        return JsonResponse(product)


@login_required_decorator
def category_page(request):
    categories = Category.objects.all()
    ctx = {
        "categories": categories
    }
    return render(request, "dashboard/category/category.html", ctx)


@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("category_page")
    ctx = {
        "model": model,
        "form": form,
    }
    return render(request, "dashboard/category/form.html", ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("category_page")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/category/form.html", ctx)

@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect("category_page")


@login_required_decorator
def product_page(request):
    products = Product.objects.all().order_by("-created_at")
    ctx = {
        "products": products,
    }
    return render(request, "dashboard/product/product.html", ctx)

@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("product_page")
    ctx = {
        "model": model,
        "form": form,
    }
    return render(request, "dashboard/product/form.html", ctx)

@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(pk=pk)
    print(model)
    form = ProductForm(request.POST or None, request.FILES or None, instance=model)
    print(form)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("product_page")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "dashboard/product/form.html", ctx)

@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect("product_page")
