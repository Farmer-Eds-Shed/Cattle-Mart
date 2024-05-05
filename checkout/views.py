from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    trailer = request.session.get('trailer', {})
    if not trailer:
        messages.error(request, "There's nothing in your trailer at the moment")
        return redirect(reverse('cattle'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)