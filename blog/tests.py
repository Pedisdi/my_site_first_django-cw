from django.test import TestCase, Client

# from django.urls import get_resolver
#
# print(get_resolver())
from django.urls import reverse


class TestViewHome(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("blog-home-without-color"))
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name_args(self):
        response = self.client.get(reverse("blog-home", args=("red",)))

        self.assertEqual(response.status_code, 200)


class TestViewAbout(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_url_exists_at_correct_location_about(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name_about(self):
        response = self.client.get(reverse("blog-about-without-color"))
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name_args_about(self):
        response = self.client.get(reverse("blog-about", args=("blue",)))
        self.assertEqual(response.status_code, 200)


class TestViewContact(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_url_exists_at_correct_location_contact(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name_contact(self):
        response = self.client.get(reverse("blog-contact"))
        self.assertEqual(response.status_code, 200)

    def test_content_availability(self):
        response = self.client.get(reverse("blog-contact"))
        self.assertContains(response, "<h1>Contact</h1>")

    def test_template_availability(self):
        response = self.client.get(reverse("blog-contact"))
        self.assertTemplateUsed(response, "contact.html")


class TestViewColor(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_url_exists_at_correct_location_view_color(self):
        response = self.client.get("/color/red/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name_view_color(self):
        response = self.client.get(reverse("blog-color", args=("red",)))
        self.assertEqual(response.status_code, 200)
