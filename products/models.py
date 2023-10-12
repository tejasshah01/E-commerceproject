from django.db import models
import datetime

# Create your models here.

class category_brand(models.Model):
    Category=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Category}"
    @staticmethod
    def get_all_categories():
        return category_brand.objects.all()
    

class products(models.Model):
    Category=models.ForeignKey(category_brand,on_delete=models.CASCADE)
    Item_name=models.CharField(max_length=100)
    Brand=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='user_profile')
    Price=models.DecimalField(max_digits=20,decimal_places=2)
    date=models.DateField(default=datetime.date.today)
    

    def __str__(self):
        return f"{self.Brand}-{self.Item_name}-{self.Price}"

    
    @staticmethod
    def get_products_by_id(ids):
        return products.objects.filter (id__in=ids)
    
    @staticmethod
    def get_all_products():
        return products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(Category_id):
        if Category_id:
            return products.objects.filter (Category=Category_id)
        else:
            return products.get_all_products()
        

