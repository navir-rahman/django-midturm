from typing import Any
from django.shortcuts import render
from brand.models import BrandModel
from car.models import CarModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
# Create your views here.

def home(request, brand_slug=None):
    cars = CarModel.objects.all()
    brands = BrandModel.objects.all()
    if brand_slug is not None:
        brand_queryset = BrandModel.objects.filter(brand_name=brand_slug)
        if brand_queryset.exists():
            brand_ = brand_queryset.first()
            cars = CarModel.objects.filter(brand=brand_)

    return render(request, 'home.html', {'brands': brands, 'cars': cars})


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'all_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, self.object)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Registration failed. Please check the form for errors.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        btn_text = super().get_context_data(**kwargs)
        btn_text['btn_text'] = 'Sign Up.'
        return btn_text

class SignInView(LoginView):
    form_class = AuthenticationForm
    template_name = 'all_form.html'
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'your information is incorrect. Please check the form for errors.')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        btn_text = super().get_context_data(**kwargs)
        btn_text['btn_text'] = 'Sign In.'
        return btn_text
    


