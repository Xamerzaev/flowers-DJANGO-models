from django.contrib import admin
from .models import Transactions, User, Flowerlot


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_type']
    fields = ['username', 'user_type']


admin.site.register(User, UserAdmin)


class FlowerlotAdmin(admin.ModelAdmin):
    list_display = ['kind', 'shade', 'quantity',
                    'price']


admin.site.register(Flowerlot, FlowerlotAdmin)


admin.site.register(Transactions)
