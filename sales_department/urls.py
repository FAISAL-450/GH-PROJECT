from django.urls import include, path
from .views import sales_department_view
urlpatterns = [
    path('', sales_department_view, name='sales_department'),
    path('customer/', include('customer.urls')),        # ✅ Ensures projects are accessible
]
