from django.contrib import admin
from .models import Cattle, Enterprise, Breed, StockType

# Register your models here.
admin.site.register(Cattle)
admin.site.register(Enterprise)
admin.site.register(Breed)
admin.site.register(StockType)
