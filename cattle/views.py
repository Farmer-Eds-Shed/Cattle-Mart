from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Cattle, Enterprise, StockType
from django.db.models.functions import Lower
from .forms import CattleForm


# Create your views here.

def all_cattle(request):
    """ A view to show all cattle, including sorting and search queries """

    cattle = Cattle.objects.all()
    query = None
    enterprises = None
    stock_types = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                cattle = cattle.annotate(lower_name=Lower('name'))
            if sortkey == 'enterprise':
                sortkey = 'enterprise__name'
            if sortkey == 'stock_type':
                sortkey =='stock_type__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            cattle = cattle.order_by(sortkey)
            
        if 'enterprise' in request.GET:
            enterprises = request.GET['enterprise'].split(',')
            cattle = cattle.filter(enterprise__name__in=enterprises)
            enterprises = Enterprise.objects.filter(name__in=enterprises)

        if 'stock_type' in request.GET:
            stock_types = request.GET['stock_type'].split(',')
            cattle = cattle.filter(stock_type__name__in=stock_types)
            stock_types = StockType.objects.filter(name__in=stock_types)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('cattle'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            cattle = cattle.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'cattle': cattle,
        'search_term': query,
        'current_enterprise': enterprises,
        'current_sorting': current_sorting,
    }

    return render(request, 'cattle/cattle.html', context)


def cattle_detail(request, cattle_id):
    """ A view to show individual cattle details """

    cattle = get_object_or_404(Cattle, pk=cattle_id)

    context = {
        'cattle': cattle,
    }

    return render(request, 'cattle/cattle_detail.html', context)

def add_cattle(request):
    """ Add cattle to mart """
    if request.method == 'POST':
        form = CattleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added animal!')
            return redirect(reverse('add_cattle'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = CattleForm()
    
    template = 'cattle/add_cattle.html'
    context = {
        'form': form,
    }

    return render(request, template, context)