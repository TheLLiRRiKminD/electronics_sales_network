from django.contrib import admin

from suppliers.models import NetworkMember, Product


@admin.register(NetworkMember)
class NetworkMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'supplier')
    list_filter = ('city',)

    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class NetworkMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')