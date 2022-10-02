from django.urls import path, re_path
from mainapp import views

urlpatterns = [
    # Landing pages
    path("", views.index),


    # Auth pages
    path("reg/", views.reg),
    path("auth/", views.auth),


    # Work area

    # Dashboard page
    path("dashboard/", views.dashboard),

    # Order pages
    re_path(r"^orders/", views.orders,),
    re_path(r"^one_order/", views.one_order,),
    re_path(r"^order_create/", views.order_create,),
    re_path(r"^order_edit/", views.order_edit,),

    # Courier pages
    re_path(r"^couriers/", views.couriers),
    re_path(r"^one_courier/", views.one_courier),
    re_path(r"^courier_create/", views.courier_create),
    re_path(r"^courier_edit/", views.courier_edit),

    # Product pages
    re_path(r"^products/", views.products),
    re_path(r"^one_product/", views.one_product),
    re_path(r"^product_create/", views.product_create),
    re_path(r"^product_edit/", views.product_edit),

    re_path(r"^qotaq/", views.index),
]