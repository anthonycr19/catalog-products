from django.db import models
from django.utils.translation import gettext_lazy as _
from .utils import create_ramdom_string


class Product(models.Model):
    """
    Product Model storage a product register
    """
    SKU_LENGTH = 15

    sku = models.CharField(
        _('SKU'),
        max_length=SKU_LENGTH,
        primary_key=True,
    )
    name = models.CharField(
        _('name'),
        max_length=50,
    )
    price = models.FloatField(
        _('price'),
        default=0,
    )
    brand = models.CharField(
        _('brand'),
        max_length=150,
        blank=True,
        null=True,
        help_text=_('literal brand name')
    )

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.create_sku()
        super(Product, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return f'{self.sku} - {self.name}'

    def create_sku(self):
        """generate random sku only create"""
        if self._state.adding:
            self.sku = create_ramdom_string(length=self.SKU_LENGTH)


class LogUserReadProduct(models.Model):
    product = models.ForeignKey(
        Product,
        models.CASCADE,
        verbose_name=_('product')
    )
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Log user read product')
        verbose_name_plural = _('Logs users read products')

    def __str__(self):
        return f'{self.product.name} visto el {self.date_created.strftime("%m/%d/%Y, %H:%M:%S")}'
