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
        price (Int): Price of the item in Euros € TTC/VAT included
    """
    name_text = models.CharField(max_length=50)
    description_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")
    work_duration = models.DurationField("Work time needed")
    material_list = models.JSONField(default=dict({'Cloth' : 'A lot'}))
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
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    reduction_percentage = models.IntegerField(default=0)
    number_available = models.IntegerField(default=0)
    def __str__(self):
        return str(self.item.name_text) + " stock is " + str(self.number_available)
    
class Commission (models.Model):
    """Commission model to take on customized requests

    Args:
        itemname_text (string): Title of the asked product 
        description_text (string): Description of the item with reference links
        features_text (string): Key features of the commission, height, color, feeling...
        deadline_date (datetime): Deadline of the commission
        budget_float (float): Price for the commission
        username_text (string): Name of the client
        email_text (string): Email of the client
        contact_text (string): Other contact means if needed
    """
    
    itemname_text = models.CharField('Name of Commission', max_length=50)
    description_text = models.CharField('Description', max_length=300, default='')
    features_text = models.CharField('Specific Features', max_length=200, default='')
    deadline_date = models.DateTimeField("Deadline (format YYYY-MM-DD)")
    budget_float = models.FloatField('Budget' ,default=50)
    username_text = models.CharField('Name' , max_length=50)
    email_text = models.CharField('Email', max_length=50)
    contact_text = models.CharField('Other ways to contact', max_length=200, default='')
    
    def __str__(self):
        return self.itemname_text