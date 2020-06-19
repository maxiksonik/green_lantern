from django.views import View
from django.shortcuts import render

from apps.cars.models import Car


class CarsView(View):

    def get(self, request, car_id=None):
        cars = Car.objects.all()
        if car_id:
            car = Car.objects.get(id=car_id)
            return render(request, 'car_detail.html', {'car': car})
        return render(request, 'all_cars.html', {'list_of_cars': cars})


class DealerCarListView(View):

    def get(self, request, dealer_id=None):
        cars = Car.objects.filter(dealer_id=dealer_id)
        return render(request, 'cars_of_dealer.html', {'list_of_cars': cars})
