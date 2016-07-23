from django.test import TestCase
from django.test.client import Client
from .models import User
from django.core.urlresolvers import reverse

# Create your tests here.
class UserTestCase(TestCase):

    fixtures = ["users.json"]
    url_list = reverse("users:user_list")
    url_create = reverse("users:create_user")
    data = {
        "password": "12345",
        "last_login": None,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@doe.dk",
    }

    def test_create(self):
        c = Client()

        #Check if user matching the one we create is not already there
        queryset = User.objects.filter(email = "john@doe.dk")
        self.assertEqual(len(queryset), 0)
        #Create new user with data
        response = c.post(self.url_create, self.data)
        #Check if user is there now
        queryset = User.objects.filter(email = "john@doe.dk", first_name = "John", last_name = "Doe")
        self.assertEqual(len(queryset), 1)

    def test_unique_email(self):
        c = Client()
        data = self.data.copy()
        data["email"] = "po@getbundl.com"

        #Check if user with email matching the one we create is already there
        queryset = User.objects.filter(email = "po@getbundl.com")
        self.assertEqual(len(queryset), 1)
        #Create new user with data
        response = c.post(self.url_create, data)
        #Check if user with email is still there
        queryset = User.objects.filter(email = "po@getbundl.com")
        self.assertEqual(len(queryset), 1)
        # Check if new user with data and same email was created
        queryset = User.objects.filter(email = "po@getbundl.com", first_name = "John", last_name = "Doe")
        self.assertEqual(len(queryset), 0)

    def test_list(self):
        c = Client()
        response = c.get(self.url_list)
        users = response.context["object_list"]
        #Check if length of users list is true
        self.assertEqual(len(users),2)
        #Check if data of the users is true
        self.assertEqual(users[0].email, "po@getbundl.com")
        self.assertEqual(users[1].email, "philip.femo@gmail.com")
