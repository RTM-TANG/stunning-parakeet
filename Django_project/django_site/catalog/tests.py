from django.test import TestCase
from django.urls import reverse
from .models import Item, Commission, Stock
from datetime import timedelta, date
# Create your tests here.

def create_Item(name, description, publication, duration, price):
    """
    Creates and Return an Item object
    """
    return Item.objects.create(name_text=name, 
                               description_text=description,
                               pub_date=publication,
                               work_duration=duration,
                               price=price
                               )
    
def create_Commission(itemname, description, features, deadline, budget, username, email, contact):
    """Creates a Commission object

    Args:
        itemname (string): name of the item
        description (string):  Description and characteristics of the item
        features (string): Features wanted on the commissioned item
        deadline (datetime.datetime): Last date to finish the commission
        budget (float): Money
        username (string): Name of the client
        email (string): Mail of the client
        contact (string): Other ways to contact the client

    Returns:
        Commission: Class that represents a command for a plush 
    """
    return Commission.objects.create(itemname_text=itemname, 
                               description_text=description,
                               features_text=features,
                               deadline_date=deadline,
                               budget_float=budget,
                               username_text=username,
                               email_text = email,
                               contact_text=contact
                               )
    
    
class CatalogIndexViewTest(TestCase) :
    def test_noItems_noCommission(self):
        """
        If no items and no commissions exist, an appropriate image is displayed
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='No item listed')
        self.assertContains(response, text='No active commission')
        
    def test_noCommission(self):
        """
        If no commissions exist, an appropriate image is displayed
        """
        item = create_Item("exemple_of_item", "description uwu", "2024-06-09", timedelta(2), 50)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No active commission')
        self.assertContains(response, 'exemple_of_item')
    
    def test_noItems(self):
        """
        If no items exist, an appropriate image is displayed
        """
        commission = create_Commission("exemple_of_commission", 'description exemple', 'no features', date(2025, 11, 6), 50, 'TestRobot', 'NoEmail', 'Django')
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No item listed')
        self.assertContains(response, 'exemple_of_commission')
        
    def test_Items_and_Commissions(self):
        """
        If items and commissions exist, their names are displayed in the view
        """
        item = create_Item("exemple_of_item", "description uwu", "2024-06-09", timedelta(2), 50)
        item2 = create_Item("Theory of Beauty", "good song", "2024-12-09", timedelta(5), 50)
        commission = create_Commission("exemple_of_commission", 'description exemple', 'no features', date(2025, 11, 6), 50, 'TestRobot', 'NoEmail', 'Django')
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'exemple_of_item')
        self.assertContains(response, 'Theory of Beauty')
        self.assertContains(response, 'exemple_of_commission')
        
        

        
    
        
        