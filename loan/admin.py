from django.contrib import admin
from .models import LoanResults
from .models import cardResults
from .models import cardResult

admin.site.register(LoanResults)
admin.site.register(cardResults)
admin.site.register(cardResult)