from urllib import request
from django.template.response import TemplateResponse
# from django.http import HttpResponse


def index(request):
    return TemplateResponse(request, "index.html")


def reg(est):
    return TemplateResponse(request, "reg.html")


def auth(reqest):
    return TemplateResponse(request, "auth.html")


def dashboard(reqest):
    return TemplateResponse(request, "dashboard.html")


def orders(reqest):
    return TemplateResponse(request, "orders.html")


def one_order(reqest):
    return TemplateResponse(request, "one_order.html")


def order_create(reqest):
    return TemplateResponse(request, "order_create.html")


def order_edit(reqest):
    return TemplateResponse(request, "order_edit.html")


def couriers(reqest):
    return TemplateResponse(request, "couriers.html")


def one_courier(est):
    return TemplateResponse(request, "one_courier.html")


def courier_create(reqest):
    return TemplateResponse(request, "courier_create.html")


def courier_edit(reqest):
    return TemplateResponse(request, "courier_edit.html")


def products(reqest):
    return TemplateResponse(request, "products.html")


def one_product(est):
    return TemplateResponse(request, "one_product.html")


def product_create(reqest):
    return TemplateResponse(request, "product_create.html")


def product_edit(reqest):
    return TemplateResponse(request, "product_edit.html")
