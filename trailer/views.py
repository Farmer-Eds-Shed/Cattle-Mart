from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from cattle.models import Cattle

# Create your views here.

def view_trailer(request):
    """ A view that renders the trailer contents page """

    return render(request, 'trailer/trailer.html')


def add_to_trailer(request, cattle_id):
    """ Add a quantity of the specified product to the trailer """

    redirect_url = request.POST.get('redirect_url')
    trailer = request.session.get('trailer', {})
    animal = Cattle.objects.get(pk=cattle_id)
    quantity = int(request.POST.get('quantity'))

    if cattle_id in list(trailer.keys()):
        trailer[cattle_id] += quantity
    else:
        trailer[cattle_id] = quantity
        messages.success(request, f'Added {animal.stock_type} to your trailer')

    request.session['trailer'] = trailer
    print(request.session['trailer'])
    return redirect(redirect_url)


def adjust_trailer(request, cattle_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    animal = Cattle.objects.get(pk=cattle_id)
    trailer = request.session.get('trailer', {})

    if quantity > 0:
        trailer[cattle_id] = quantity
        messages.success(request, f'Updated {animal.stock_type} in your trailer')
    else:
        trailer.pop(cattle_id)
        messages.success(request, f'Removed {animal.stock_type} from your trailer')

    request.session['trailer'] = trailer
    return redirect(reverse('view_trailer'))


def remove_from_trailer(request, cattle_id):
    """Remove the item from the trailer"""

    try:
        trailer = request.session.get('trailer', {})
        animal = Cattle.objects.get(pk=cattle_id)
        trailer.pop(cattle_id)
        messages.success(request, f'Removed {animal.stock_type} from your trailer')

        request.session['trailer'] = trailer
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)