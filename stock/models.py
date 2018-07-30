from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_id = models.CharField(max_length=50)
    cat_stock = models.PositiveIntegerField()
    cat_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('stock:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.cat_name

class Product(models.Model):
    pr_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pr_id = models.CharField(max_length=100)
    pr_name = models.CharField(max_length=500)
    pr_price = models.DecimalField(max_digits = 10, decimal_places=2)
    pr_stock = models.PositiveIntegerField()
    pr_image = models.ImageField()
    pr_mfg = models.DateTimeField(default=timezone.now())
    pr_avb = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('stock:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.pr_name




