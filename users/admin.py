from django.contrib import admin

from users.models import User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    """
    Интерфейс администратора для модели User.
    """
    list_display = ('id', 'first_name')
