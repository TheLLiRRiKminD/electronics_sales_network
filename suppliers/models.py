from django.db import models

NULLABLE = {'blank': True, 'null': True}


class NetworkMember(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    hierarchy_level = models.IntegerField(default=0)

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
    network_member = models.ForeignKey(NetworkMember, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} ({self.model})"
