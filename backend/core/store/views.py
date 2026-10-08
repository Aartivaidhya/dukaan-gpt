from django.shortcuts import render
from .models import KiranaItem

def dashboard(request):
    items = KiranaItem.objects.all()
    total_stock = sum([i.quantity_in_stock for i in items])
    return render(request, 'store/dashboard.html', {'items': items, 'total_stock': total_stock})