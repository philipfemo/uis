from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from users.models import User
from products.models import Product, Category

class ProductTestCase(TestCase):

    fixtures = ["categories.json", "products.json", "users.json"]
    url_list = reverse("products:productslist")
    url_manage = reverse("products:products_manage")
    url_create = reverse("products:product_create")
    url_catcreate = reverse("products:category_create")
    data = {
        "title": "test product",
        "description": "testing",
        "category": 1,
        "price": 10,
        "stock": 10}
    data2 = {
        "category": "test cat"}
    data3 = {
        "form-TOTAL_FORMS":2,
        "form-INITIAL_FORMS":2,
        "form-MIN_NUM_FORMS":0,
        "form-MAX_NUM_FORMS":1000,
        "form-0-stock":2000,
        "form-0-id":1,
        "form-1-stock":2000,
        "form-1-id":2
    }
    def test_categories(self):
        c = Client()
        queryset = Category.objects.filter( category = "test cat")
        self.assertEqual(len(queryset), 0)
        response = c.post(self.url_catcreate, self.data2)
        queryset = Category.objects.filter( category = "test cat")
        self.assertEqual(len(queryset), 1)



    def test_create(self):
        c = Client()

        #Check if product matching the one we create is not already there
        queryset = Product.objects.filter( title = "test product")
        self.assertEqual(len(queryset), 0)
        #Create new product with data
        response = c.post(self.url_create, self.data)
        #Check if product exists now
        queryset = Product.objects.filter(
            title = "test product",
            description = "testing",
            category = 1,
            price = 10,
            stock = 10
            )
        self.assertEqual(len(queryset), 1)

    def test_productslist(self):
        c = Client()
        response = c.get(self.url_list)
        products = response.context["object_list"]
        #Check if length of users list is true
        self.assertEqual(len(products),2)
        #Check if data is true
        self.assertEqual(products[0].title, "test product 1")
        self.assertEqual(products[1].title, "test product 2")

    def test_productslist_create(self):
        c = Client()
        response = c.get(self.url_list)
        products = response.context["object_list"]
        #Check if length of users list is true
        self.assertEqual(len(products),2)
        #Check if data is true
        self.assertEqual(products[0].title, "test product 1")
        self.assertEqual(products[1].title, "test product 2")

        #Create new product
        response = c.post(self.url_create, self.data)

        #Test if list updated
        response = c.get(self.url_list)
        products = response.context["object_list"]
        self.assertEqual(len(products),3)

    def test_manage(self):
        c = Client()
        user = User.objects.get(pk = 1)
        c.force_login(user)
        response = c.get(self.url_list)
        products = response.context["object_list"]
        self.assertEqual(products[0].stock, 5)
        self.assertEqual(products[1].stock, 15)

        response = c.post(self.url_manage, self.data3)

        response = c.get(self.url_list)
        products = response.context["object_list"]
        self.assertEqual(products[0].stock, 2000)
        self.assertEqual(products[1].stock, 2000)
