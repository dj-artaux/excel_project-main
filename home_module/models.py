from django.db import models



class ProductTable(models.Model):
    title = models.CharField(max_length=300,verbose_name='Nom du produit')
    price = models.IntegerField(verbose_name='prix du produit')
    count = models.IntegerField(verbose_name='Nombre de produits')
    is_active = models.BooleanField(verbose_name='inventaire')
