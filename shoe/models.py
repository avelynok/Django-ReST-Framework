from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return self.name

class ShoeType(models.Model):
    types = [
        ('SK', 'Sneaker'),
        ('B', 'Boot'),
        ('SD', 'Sandal'),
        ('D', 'Dress'),
        ('O', 'Other')
    ]
    style = models.CharField(max_length=30, choices=types, blank=False)

    def __str__(self):
        return self.style
    
class ShoeColor(models.Model):
    colors = [
        ('R', 'red'),
        ('O', 'orange'),
        ('Y', 'yellow'),
        ('G', 'green'),
        ('B', 'blue'),
        ('I', 'indigo'),
        ('V', 'violet'),
        ('B', 'black'),
        ('W', 'white'),
    ]
    color_name = models.CharField(max_length=30, choices=colors,blank=False)

    def __str__(self):
        return self.color_name
    
class Shoe(models.Model):
    size = models.IntegerField()
    brand = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor,on_delete= models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)
    
        