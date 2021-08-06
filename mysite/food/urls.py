from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home_page"),
    path("add_product/", get_data, name="get_data"),
    path("admin/", admin_page, name="admin_page"),

    path("login/", login_page, name="login_page"),
    path("logout/", logout_page, name="logout"),

    path("admin/category", category_page, name="category_page"),
    path("admin/category/create", category_create, name="category_create"),
    path("admin/category/edit/<int:pk>", category_edit, name="category_edit"),
    path("admin/category/delete/<int:pk>", category_delete, name="category_delete"),

    path("admin/product", product_page, name="product_page"),
    path("admin/product/create", product_create, name="product_create"),
    path("admin/product/edit/<int:pk>", product_edit, name="product_edit"),
    path("admin/product/delete/<int:pk>", product_delete, name="product_delete"),

]
