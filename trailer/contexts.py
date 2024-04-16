from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from cattle.models import Cattle

def trailer_contents(request):

    trailer_cattle = []
    total = 0
    cattle_count = 0

    trailer = request.session.get('trailer', {})


    for cattle_id, quantity in trailer.items():
        cattle = get_object_or_404(Cattle, pk=cattle_id)
        total += quantity * cattle.price
        cattle_count += quantity
        trailer_cattle.append({
            'cattle_id': cattle_id,
            'quantity': quantity,
            'cattle': cattle,
        })
    
    context = {
        'trailer_cattle': trailer_cattle,
        'total': total,
        'cattle_count': cattle_count,
    }

    return context