from rest_framework.test import APITestCase
from django.urls import reverse

#if the registration data is correct
#if the password is invalid
#if the username is already taken
#If a member is logged in, that page should not appear
#403 error should be received if a member logged in with token

class UseerRegistrationTesrCase(APITestCase):
    url = reverse("account:register")

    def test_user_registration(self):
        """
        if the registration data is correct
        """

        data ={
            "username" : "ozaytest",
            "password" : "passwordtest"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)