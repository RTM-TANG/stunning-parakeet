""" Tests of the application catalog """

from django.test import TestCase
from django.urls import reverse
from .models import Item, Commission, Stock
from datetime import timedelta, date, datetime
from django.utils import timezone
from .forms import CommissionForm

def create_Item(name, description, publication, duration, price):
    """
    Creates and Return an Item object
    
    :param name: Name of the item
    :type name: string
    :param description: Description and characteristics of the item
    :type description: string
    :param publication: Date of publication of the item
    :type publication: datetime.datetime
    :param duration: Time estimated to produce one item
    :type duration: timedelta  
    :param Price: Price in € that the customer is ready pay
    :type Price: float
    :return: Returns an object of the Item Class
    :rtype: Item
    """
    return Item.objects.create(name_text=name, 
                               description_text=description,
                               pub_date=publication,
                               work_duration=duration,
                               price=price
                               )
    
def create_Commission(itemname, description, features, deadline, budget, username, email, contact):
    """
    Creates a Commission object

    :param itemname: Name of the item
    :type itemname: string
    :param description: Description and characteristics of the commission
    :type description: string
    :param features: Features wanted on the commissioned item
    :type features: string
    :param deadline: Last date to finish the commission
    :type deadline: datetime.datetime
    :param budget: Price in € that the customer is ready pay
    :type budget: float
    :param username: Name of the client
    :type username: string
    :param email: Mail of the client
    :type email: string
    :param contact: Alternative ways to contact the client
    :type contact: string
    :return: Returns an object of the Commission Class
    :rtype: Commission
    
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
    
class CatalogFormsTest(TestCase):
    def test_ErrorCommissionForm(self):
        """
        If the data inside the form is wrong, an error will generate
        """
        form_data = {'error': 80085}
        form = CommissionForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_CommissionForm(self):
        """
        If the data ot the right typings, the form is validated
        """
        form_data = {'itemname_text': 'Plush-name', 
                     "description_text": 'description', 
                     "features_text": 'feats', 
                     "deadline_date": timezone.now(), 
                     "budget_float": 50, 
                     "username_text": 'Jojo', 
                     "email_text": 'Bizarre', 
                     "contact_text": 'Adventure'}
        form = CommissionForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    
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
        item = create_Item("exemple_of_item", "description uwu", timezone.now(), timedelta(2), 50)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No active commission')
        self.assertContains(response, 'exemple_of_item')
    
    def test_noItems(self):
        """
        If no items exist, an appropriate image is displayed
        """
        commission = create_Commission("exemple_of_commission", 'description exemple', 'no features', timezone.now() + timedelta(50), 50, 'TestRobot', 'NoEmail', 'Django')
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No item listed')
        self.assertContains(response, 'exemple_of_commission')
        
    def test_Items_and_Commissions(self):
        """
        If items and commissions exist, their names are displayed in the view
        """
        item = create_Item("exemple_of_item", "description uwu", timezone.datetime(2026,12,13), timedelta(2), 50)
        item2 = create_Item("Theory of Beauty", "good song", timezone.datetime(2024,12,9), timedelta(5), 50)
        commission = create_Commission("exemple_of_commission", 'description exemple', 'no features', date(2025, 11, 6), 50, 'TestRobot', 'NoEmail', 'Django')
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'exemple_of_item')
        self.assertContains(response, 'Theory of Beauty')
        self.assertContains(response, 'exemple_of_commission')

class CatalogCommissionCreateViewTest(TestCase):
    def test_noforms(self):
        """Checks if we get the page if we go into the url
        """
        response = self.client.get(reverse("commission-create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Budget')
        
    # def test_postforms (self):
    #     response = self.client.post(reverse("commission-create"), {'itemname_text' : 'something'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFormError(response, CommissionForm, 'itemname_text', 'This field is required.')
    
class CatalogCommissionDetailViewTest(TestCase):
    def test_response(self):
        """If a Commission Id is passed, it will display its content
        """
        test_Commission= create_Commission("exemple_of_commission", 'description exemple', 'no features', date(2025, 11, 6), 50, 'TestRobot', 'NoEmail', 'Django')
        response = self.client.get(reverse("commission-detail", args=(test_Commission.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Details de la Commission")
        self.assertContains(response, "NoEmail")
        
class CatalogItemDetailViewTest(TestCase):
    def test_response(self):
        """If an Item Id is passed, it will display the content of associated item
        """
        test_item = create_Item("Theory of Beauty", "good song", timezone.datetime(2024,12,9), timedelta(5), 50)
        response = self.client.get(reverse("commission-detail", args=(test_item.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Details du catalogue")
        self.assertContains(response, "Nom : Theory of Beauty")
        self.assertContains(response, "Description : good song")
        self.assertContains(response, "Date de publication : 2024-12-09")
        self.assertContains(response, "Temps de fabrication : 5")