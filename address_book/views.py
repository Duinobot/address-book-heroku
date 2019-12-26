from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages

# Create your views here.
def home(request):
    address_list = Address.objects.all()
    context = {'address_list' : address_list}
    return render(request, 'home.html', context=context)

def add_address(request):
    if request.method == "POST":
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Address has been added!")
            return redirect('home')
        else:
            messages.success(request,('Error there is'))
            return render(request, 'add_address.html',{})
    else:
        return render(request, 'add_address.html', {})

def edit_address(request, list_id):
    if request.method == 'POST':
        current_address = Address.objects.get(id=list_id)
        form = AddressForm(request.POST or None, instance=current_address)
        if form.is_valid():
            form.save()
            messages.success(request, ("Changed saved"))
            return redirect('home')
        else:
            messages.success(request, ("Seems like there's an error..."))
            return render(request, 'edit.html', {})
    else:
        current_address = Address.objects.get(id=list_id)
        context = {'current_address':current_address}
        return render(request, "edit.html", context=context)

def delete(request, list_id):
    if request.method == 'POST':
        address = Address.objects.get(id=list_id)
        address.delete()
        messages.success(request,('Done'))
        return redirect('home')
    else:
        messages.warning(request,('no entry'))
        return redirect('home')