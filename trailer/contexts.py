from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from cattle.models import Cattle
from django.contrib import messages


def trailer_contents(request):

    trailer_cattle = []
    total = 0
    animal_sold = False
    trailer = request.session.get('trailer', {})

    for cattle_id, quantity in trailer.items():
        cattle = get_object_or_404(Cattle, pk=cattle_id)
        total += cattle.price
        if cattle.sold == True:
            animal_sold = True
        trailer_cattle.append({
            'cattle_id': cattle_id,
            'cattle': cattle,
        })

    context = {
        'trailer_cattle': trailer_cattle,
        'total': total,
        'animal_sold': animal_sold,
    }

    return context
