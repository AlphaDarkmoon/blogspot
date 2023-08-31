from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

# Define a view for user sign-up, inheriting from CreateView
class SignUp(generic.CreateView):
    # Use the CustomUserCreationForm for user registration
    form_class = CustomUserCreationForm
    # Redirect to the login page after successful registration
    success_url = reverse_lazy("login")
    # Use the 'signup.html' template for rendering the form
    template_name = "register_new.html"
