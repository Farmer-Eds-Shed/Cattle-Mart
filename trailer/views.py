from django.shortcuts import render, redirect

# Create your views here.

def view_trailer(request):
    """ A view that renders the trailer contents page """

    return render(request, 'trailer/trailer.html')


def add_to_trailer(request, cattle_id):
    """ Add a quantity of the specified product to the trailer """

    redirect_url = request.POST.get('redirect_url')
    trailer = request.session.get('trailer', {})

    quantity = int(request.POST.get('quantity'))

    if cattle_id in list(trailer.keys()):
        trailer[cattle_id] += quantity
    else:
        trailer[cattle_id] = quantity

    request.session['trailer'] = trailer
    print(request.session['trailer'])
    return redirect(redirect_url)