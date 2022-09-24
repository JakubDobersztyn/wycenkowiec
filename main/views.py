import json

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from main.forms import ServiceForm

from main.models import Service, Pricing, PricingService


class IndexView(View):
    def get(self, request):
        services = Service.objects.all()
        return render(request, 'index.html', {'services': services})


class AddServiceView(View):
    def get(self, request):
        form = ServiceForm
        return render(request, 'add-service.html', {'form': form})

    def post(self, request):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            form = ServiceForm
            return render(request, 'add-service.html', {'form': form, 'message': 'Dodano do bazy'})
        else:
            return render(request, 'add-service.html', {'form': form})


class AddPricing(View):
    def post(self, request):
        payload = json.loads(request.body)
        # user = User.objects.get(pk=request.user.id)
        user = User.objects.get(pk=1)
        pricing = Pricing.objects.create(client=payload['client_name'], user=user)
        for service in payload['services']:
            if service['service_id']:
                service_object = Service.objects.get(pk=service['service_id'])
                PricingService.objects.create(service=service_object, pricing=pricing, quantity=service['quantity'])
        return JsonResponse({'pricing_id': pricing.id})


class PricingDetailsView(View):
    def get(self, request, id):
        pricing = Pricing.objects.get(pk=id)
        services = PricingService.objects.filter(pricing=pricing)
        sum = 0
        for service in services:
            cost = service.quantity * service.service.unit_price
            service.cost = round(cost, 2)
            sum += service.cost

        return render(request, "pricing_details.html", {'pricing': pricing, 'services': services, 'sum': sum})


class UserPricings(View):
    def get(self, request):
        # user = User.objects.get(pk=request.user.id)
        user = User.objects.get(pk=1)
        pricings = Pricing.objects.filter(user=user)
        return render(request, "user_pricings.html", {'pricings': pricings})