from django.shortcuts import render

# Create your views here.

def view_trailer(request):
    """ A view that renders the trailer contents page """

    return render(request, 'trailer/trailer.html')
