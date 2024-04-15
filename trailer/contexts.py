from decimal import Decimal
from django.conf import settings

def trailer_contents(request):

    trailer_cattle = []
    total = 0
    cattle_count = 0

    
    context = {
        'trailer_cattle': trailer_cattle,
        'total': total,
        'cattle_count': cattle_count,
    }

    return context