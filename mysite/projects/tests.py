from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from users.models import User
from projects.models import Project
# Create your tests here.
class ProjectTestCase(TestCase):

    fixtures = ["users.json", "projects.json"]
    url_list = reverse("projects:projectslist")
    url_create = reverse("projects:project_create")
    data = {
        "title" : "TestProject",
        "description" : "Some Test Project"
    }

    def test_list_requires_authentication(self):
        c = Client()
        response = c.get(self.url_list)

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.url.find("login"), -1)


    def test_create_requires_authentication(self):
        c = Client()

        # attempt to create while not logged in - expects redirect
        response = c.post(self.url_create, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.url.find("login"), -1)

    def test_create(self):
        user = User.objects.get(pk = 1)
        c = Client()
        c.force_login(user)

        #Check if project matching the one we create is not already there
        queryset = Project.objects.filter(title = "TestProject", description = "Some Test Project")
        self.assertEqual(len(queryset), 0)
        #Create new project with data
        response = c.post(self.url_create, self.data)
        self.assertEqual(response.url.find("login"), -1)
        #Check if project is there
        queryset = Project.objects.filter(title = "TestProject", description = "Some Test Project")
        self.assertEqual(len(queryset), 1)

    def test_list(self):
        user = User.objects.get(pk = 1)
        c = Client()
        c.force_login(user)

        response = c.get(self.url_list)
        projects = response.context["object_list"]
        self.assertEqual(len(projects), 2)
        self.assertEqual(projects[0].title, "Algebra")
        self.assertEqual(projects[1].title, "Algorithms")
