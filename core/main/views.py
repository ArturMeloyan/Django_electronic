from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from .models import HomeSlider, HomeSliderActive, HomeInfo, HomeProduct, HomeCustomerActive, HomeCustomer, About
# Create your views here.


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Hajoxutyamb grancvel eq!')
            return redirect('home')
        messages.error(request, 'Cheq grancvel, grel eq sxal informacia!!!')
    form = NewUserForm()
    return render(request=request, template_name='register.html', context={'register_form':form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request,'Duq login eq exel!!')
                return redirect('home')
            else:
                messages.error(request, 'Voch valid informacia!!!')
        else:
            messages.error(request, 'Sxal info!!!')
    form = AuthenticationForm()
    return render(request=request, template_name='login.html', context={'login_form':form})

def logout_request(request):
    logout(request)
    messages.info(request, 'Duq logout exaq!')
    return redirect('home')

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homeslider = HomeSlider.objects.all()
        homeslideractive = HomeSliderActive.objects.all()
        homeinfo = HomeInfo.objects.all()
        homeproduct = HomeProduct.objects.all()
        homecustomeractive = HomeCustomerActive.objects.all()
        homecustomer = HomeCustomer.objects.all()

        return render(request, self.template_name, {'homeslideractive':homeslideractive, 'homeslider':homeslider, 'homeinfo':homeinfo, 'homeproduct':homeproduct, 'homecustomeractive':homecustomeractive, 'homecustomer':homecustomer})


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        about = About.objects.all()
        return render(request, self.template_name, {'about':about})



class ComputerListView(ListView):
    template_name = 'computer.html'

    def get(self, request):
        return render(request, self.template_name)



class ContactListView(ListView):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)



class LaptopListView(ListView):
    template_name = 'laptop.html'

    def get(self, request):
        return render(request, self.template_name)



class ProductListView(ListView):
    template_name = 'product.html'

    def get(self, request):
        return render(request, self.template_name)