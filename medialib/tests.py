from django.test import TestCase
from .models import User, Videogame
from django.urls import reverse

def create_user():
      #Create a user with the following username, email and password
      user = User.objects.create_user(
         username='testuser', 
         email='test@test.com', 
         password='Testpassword123!')
      return user

class RegisterFormViewTests(TestCase):
   def test_create_user(self):
      # Simulate a GET request to the create_user view
      response = self.client.get(reverse('medialib:create.user'))
      # Check that the response is a redirect to the login page
      self.assertEqual(response.status_code, 200)
      # Check that the template used is the create_user.html template
      self.assertTemplateUsed(response, 'medialib/user/create_user.html')

   def test_create_user_post(self):
      # Simulate a POST request to the create_user view
      response = self.client.post(reverse('medialib:create.user'), 
         {
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'Testpassword123!',
            'password2': 'Testpassword123!'
         })
      # Check that the response is a redirect to the login page
      self.assertEqual(response.status_code, 302)
      #Check that the redirection is to the login page
      self.assertRedirects(response, reverse('medialib:login'))
      # Check that the user was created successfully
      self.assertEqual(User.objects.count(), 1)
   
   def test_user_with_used_username(self):
      """
      Test that a user that provides a already existing username cannot be registered"""
      # Create a user with the username 'testuser' that already exists in the database
      create_user()
      # Simulate a POST request to the create_user view with the same username
      response = self.client.post(reverse('medialib:create.user'), 
         {
            'username': 'testuser',
            'email': 'test2@test.com',
            'password1': 'Testpassword123!',
            'password2': 'Testpassword123!'
         })
      # Check that the response is 200 code error because the form is not valid
      self.assertEqual(response.status_code, 200)
      # Check that the user was not created
      self.assertEqual(User.objects.count(), 1)
   
   def test_passwords_dont_match(self):
      """
      Test that a iser cannot be registered if the submitted passwords don't match
      """
      # Simulate a POST request to the create_user view with the passwords don't match
      response = self.client.post(reverse('medialib:create.user'),
         {
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'Testpassword123!',
            'password2': 'Passwordtest123!'
         })
      # Check that the response is 200 code error
      self.assertEqual(response.status_code, 200)
      #Check that the user was not created
      self.assertEqual(User.objects.count(), 0)

class LoginFormViewTests(TestCase):
   def test_login_get(self):
      """
      Test that a user can access to the login view
      """
      # Simulate a GET request to the login view
      response = self.client.get(reverse('medialib:login'))
      # Check that the obtained response is a redirect to the login page
      self.assertEqual(response.status_code, 200)
      # Check that the returned template is the login.html template
      self.assertTemplateUsed(response, 'medialib/auth/login.html')
   
   def test_login_post(self):
      """
      Test that a user can log in with valid credentials
      """
      # Create a user with the following username, email and password
      user = create_user()
      # Simulate a POST request to the login view with the user's credentials
      response = self.client.post(reverse('medialib:login'),
         {
            'username': 'testuser',
            'password': 'Testpassword123!'
         })
      # Check that the response is a redirect to the home page
      self.assertEqual(response.status_code, 302)
      # Check that the loaded template is the home.html template
      self.assertRedirects(response, reverse('medialib:home'))
      # Check that the user is logged in. The user id is stored in the session under the key '_auth_user_id'
      self.assertEqual(int(self.client.session['_auth_user_id']), user.id)
   
   def test_invalid_username(self):
      """
      Test that the user cannot log in with invalid credentials
      """
      # Simulate a POST request to the login view with a non-existent username
      response = self.client.post(reverse('medialib:login'),
         {
            'username': 'nonexistentuser',
            'password': 'Testpassword123!'
         })
      # Check that the response is a 200 code error
      self.assertEqual(response.status_code, 200)
      # Check that the loaded template is the login.html template
      self.assertTemplateUsed(response, 'medialib/auth/login.html')
      # Check that the user is not logged int
      self.assertNotIn('_auth_user_id', self.client.session)

class LogoutViewTests(TestCase):
   def test_logout(self):
      """ 
      Test that a logged in user can log out successfully
      """
      # Create a user with the following username, email and password
      user = create_user()
      # Simulate the login of the user
      self.client.force_login(user)
      # Simulate a POST request to the logout view
      response = self.client.post(reverse('medialib:logout'))
      # Check that the response is a redirect to the login page
      self.assertEqual(response.status_code, 302)
      # Check that the redirection aims to the login page
      self.assertRedirects(response, reverse('medialib:login'))
      # Check that the user is not logged in
      self.assertNotIn('_auth_user_id', self.client.session)

class VideogameModelTests(TestCase):
   pass
# Create your tests here.
