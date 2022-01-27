from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    CategoryTitle = models.CharField(max_length=80)
    Slug = models.SlugField(max_length=100)
    CategoryStatus = models.BooleanField(default=True)
    Parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        self.values = f'{self.CategoryTitle}'
        return self.values

class ProductProperty(models.Model):
    PropertyTitle = models.CharField(max_length=35,primary_key=True)
    ProductPropertyStatus = models.BooleanField(default=True)

    
    def __str__(self):
        self.values = f'{self.PropertyTitle}'
        return self.values
    # Size      
    # Weight    
    # Colors    
    # Material  
    # Dimensions
    # Length    
    # Jewel     
    # Width     
    # LockType  
    # Shorten   
    # Stone     

class Attribute(models.Model):
    ProductProperty = models.ForeignKey(ProductProperty, on_delete=models.CASCADE)
    Value= models.CharField(max_length=50)
    AttributeStatus = models.BooleanField(default=True)
    
    def __str__(self):
        self.values = f'{self.ProductProperty} {self.Value}'
        return self.values

class ProductImage(models.Model):
    Image = models.CharField(max_length=220)
    
    def __str__(self):
        self.values = f'{self.Image}'
        return self.values

class Product(models.Model):
    Id = models.BigAutoField(primary_key=True ,auto_created=True)
    MainImage = models.CharField(max_length=250)
    Title = models.CharField(max_length=250)
    Brand = models.CharField(max_length=120 ,null=True, blank=True)
    Slug = models.SlugField(max_length=450)
    Description = models.TextField(null=True, blank=True)
    Price = models.CharField(max_length=35,verbose_name="Price ( $ )")
    Discount = models.IntegerField(default=0,verbose_name="Discount ( % )")
    Star = models.FloatField(null=True, blank=True)
    Image = models.ManyToManyField(ProductImage,null=True,blank=True)
    Category = models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
    Attribute = models.ManyToManyField(Attribute)
    Status = models.BooleanField(default=True)
    def CalculatePrice(self): 
        newPrice=(int(self.Price)-((int(self.Price) * self.Discount)/100))
        return newPrice
    NewPrice =CalculatePrice
    
    def __str__(self):
        self.values = f'{self.Title} {self.Brand}'
        return self.values

    