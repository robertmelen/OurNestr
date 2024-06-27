from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import QueryDict
import requests
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import House, Image
from .forms import HouseForm

# Create your views here.


class CustomLogoutView(View):
    def get(self, request):
        return render(request, 'account/logout_confirmation.html')

    def post(self, request):
        logout(request)
        return redirect('index')


def index(request):
    return render(request, template_name='core/index.html')


@login_required
def dashboard(request, pk=None):
    if request.method == 'GET':
        houses = House.objects.filter(user=request.user)
        status = House.HOUSE_STATUS_STATUS
        return render(request, template_name="core/dashboard.html", 
                  context={ 'houses': houses, 'status': status } )
    
     
#forms
def houseform(request):
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit=False)  # Save the form data to a House instance
            # Now associate the uploaded images with the house
            house.user = request.user 
            house.save()
            image = request.FILES.get("image")
            house_image = Image.objects.create(image=image)
            house.images.add(house_image)
            houses = House.objects.filter(user=request.user).order_by('-ordering_date')
            return render(request, template_name="core/htmx-partials/house-list.html", 
                  context={ 'houses': houses } )
        else:
            print(form.errors)
            return HttpResponse("Error with form")
    else:
        form = HouseForm()
        return render(request, 
                      template_name="core/partials/forms/house-form.html",
                      context={'form': form})


def delete_house(request):
    houses_selected = request.POST.getlist('house_check_id')
    for house in houses_selected:
        house = House.objects.get(pk=house)
        house.delete()
    houses = House.objects.filter(user=request.user).order_by('-ordering_date')
    response = render(request, template_name="core/htmx-partials/house-list.html", 
                  context={ 'houses': houses })
    response['HX-Refresh'] = 'true'
    return response


def edit_house(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == 'GET':
        form = HouseForm(instance=house)
        context = {'form': form, 'house': house}
        return render(request, template_name='core/partials/forms/edit-house-form.html', context=context)
    if request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = HouseForm(data, instance=house)
        if form.is_valid():
            form.save()
            response = render(request, template_name="core/dashboard.html")
            response['HX-Refresh'] = 'true'
            return response

    
def check_area(request, postcode):
    return HttpResponse('hello!')


def house_filter(request):
    if request.method == 'GET':
        status = request.GET.get('status', '')
        print(status)
        if status == 'all':
            houses = House.objects.filter(user=request.user)
        else:
            houses = House.objects.filter(status=status, user=request.user)
        return render(request, template_name="core/htmx-partials/house-list.html", 
                  context={ 'houses': houses} )
       

   