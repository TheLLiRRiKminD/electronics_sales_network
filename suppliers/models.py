from django.db import models

NULLABLE = {'blank': True, 'null': True}


class NetworkMember(models.Model):
    """
    Модель объекта NetworkMember
    """
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='E-mail')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=255, verbose_name='Номер дома')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    hierarchy_level = models.IntegerField(default=0, verbose_name='Уровень в иерархии')

    class Meta:
        verbose_name = "Участник сети"
        verbose_name_plural = "Участники сети"

    def save(self, *args, **kwargs):
        if self.supplier:
            self.hierarchy_level = self.supplier.hierarchy_level + 1
        super(NetworkMember, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель объекта Product
    """
    network_member = models.ForeignKey(NetworkMember, on_delete=models.CASCADE, verbose_name='Реализатор продукции')
    name = models.CharField(max_length=255, verbose_name='Имя')
    model = models.CharField(max_length=255, verbose_name='Модель продукта')
    release_date = models.DateField(verbose_name='Дата реализации продукта')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} ({self.model})"
