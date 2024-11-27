from django.db import models

# Create your models here.

class Item(models.Model):
    """Class representing an item in the catalog

    Args:
        name_text (string): name of the item
        description_text (string): Description and characteristics of the item
        pub_date (datetime): Date of publication of the item
        work_duration (timedelta): Time estimated to produce one item.
        material_list (JSON): List of materials/colors needed to produce one instance of the item.
        price ?
    """
    name_text = models.CharField(max_length=50)
    description_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")
    work_duration = models.DurationField("Work time needed")
    material_list = models.JSONField()
    picture_img = models.ImageField()
    price = models.IntegerField(default=20)
    def __str__(self):
        return self.name_text


class Stock(models.Model):
    """Class representing the temporary aspect of the stock
    
    Args :
        item (Item) : item linked to the stock 
        number_available (Int) : Number of stock available 
        reduction_percentage (Int) : Pourcentage de réduction temporaire
        To add
        Localisation
        Limit date of promotion
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    reduction_percentage = models.IntegerField(default=0)
    number_available = models.IntegerField(default=0)
    def __str__(self):
        return str(self.item.name_text) + " stock is " + str(self.number_available)