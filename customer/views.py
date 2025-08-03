from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm

def customer_list(request):
    """ Fetch and display customers, with optional name filtering """
    query = request.GET.get("search", "")
    customers = Customer.objects.filter(customer_name__icontains=query) if query else Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers, 'search_query': query})

def customer_form(request, customer_id=None):
    """ Handle customer creation and update """
    customer = get_object_or_404(Customer, id=customer_id) if customer_id else None
    form = CustomerForm(request.POST or None, instance=customer)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f"Customer record {'updated' if customer else 'added'} successfully!")
        return redirect('customer_list')
        
    return render(request, 'customer/customer_form.html', {'form': form, 'customer': customer})

def customer_delete(request, customer_id):
    """ Delete a customer record """
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    messages.success(request, "Customer record deleted successfully!")
    return redirect('customer_list')
