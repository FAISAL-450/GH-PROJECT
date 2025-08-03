from django.urls import path
from .views import customer_list, customer_form, customer_delete
urlpatterns = [
    path("", customer_list, name="customer_list"),
    path("form/", customer_form, name="customer_create"),
    path("form/<int:customer_id>/", customer_form, name="customer_edit"),
    path("delete/<int:customer_id>/", customer_delete, name="customer_delete"),
]
