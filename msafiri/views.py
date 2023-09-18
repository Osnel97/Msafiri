from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
import datetime
from msafiri.models import *

def index(request):
   template = loader.get_template('index.html')
   regions = Regions.objects.all().values() 
   content = {
    'regions':regions,
    'name':'Nenga',
    'time':datetime.datetime.now()
   }
   return HttpResponse(template.render(content, request))  

def add_car(request):
    template = loader.get_template('add_car.html') 
    companies = Companies.objects.all().values()
    cars = Cars.objects.all().values()
    routes = Routes.objects.all().values()
    content = {
    'cars':cars,
    'companies':companies,
    'routes':routes,
    'name':'Nenga',
    'time':datetime.datetime.now()
    }
    return HttpResponse(template.render(content, request))  

def insert_car(request):
  cars_model = request.POST['car_model']
  cars_luxury_type = request.POST['cars_luxury_type']
  cars_company_name = request.POST['cars_company_name']
  cars_route_name = request.POST['cars_route_name']
  cars_plate_no = request.POST['cars_plate_no']
  cars_date_of_journey = request.POST['cars_date_of_journey']
  cars_departure_time  = request.POST['cars_departure_time']
  cars_destination_time = request.POST['cars_destination_time']
  cars_created_time  = datetime.datetime.now()

  cars = Cars( cars_model = cars_model,
  cars_luxury_type = cars_luxury_type,
  cars_company_name = cars_company_name,
  cars_route_name = cars_route_name,
  cars_plate_no = cars_plate_no,
  cars_date_of_journey =cars_date_of_journey,
  cars_departure_time  = cars_departure_time,
  cars_destination_time = cars_destination_time,
  cars_created_time  = cars_created_time
  )
  cars.save()
  return HttpResponseRedirect(reverse('add_car'))

def delete_car(request,id):
  cars = Cars.objects.get(id=id)
  cars.delete()
  return HttpResponseRedirect(reverse('add_car'))

def routes(request):
   template = loader.get_template('routes.html') 
   no_route='no route found: modify your search.'
   regions = Regions.objects.all().values()
   route_from =''
   route_to = ''
   route=''
   date=''
   content = {
       'regions':regions,
       'no_route':no_route,
       'route':route,
       'date':date,
   }
   if  'route_from' in request.GET and 'route_to' in request.GET and 'route_date' in request.GET:
     if  request.GET['route_from']=='' and request.GET['route_to']=='' and  request.GET['route_date']=='':
       content = {
       'regions':regions,
       'no_route':no_route,
       'route':route,
       'date':date,
       }
       return HttpResponse(template.render(content, request)) 
     else:
       route_from = request.GET['route_from']
       route_to = request.GET['route_to']
       route = route_from+' - '+route_to
       date = request.GET['route_date']
       cars = Cars.objects.filter(cars_route_name=route, cars_date_of_journey=date).order_by('cars_departure_time').values()
       content = {
       'cars':cars,
       'regions':regions,
       'route':route,
       'date':date,
       }
       return HttpResponse(template.render(content, request))  
   else:
      return HttpResponse(template.render(content, request))


def about_us(request):
   template = loader.get_template('about.html') 
   content = {
   'time':datetime.datetime.now()
   }
   return HttpResponse(template.render(content, request)) 

def add_route(request):
   template = loader.get_template('add_route.html') 
   routes = Routes.objects.all().values()
   regions = Regions.objects.all().values()
   content = {
   'regions':regions,
   'routes':routes,
   'time':datetime.datetime.now()
   }
   return HttpResponse(template.render(content, request)) 

def insert_route(request):
 routes_from = request.POST['routes_from']
 routes_to =   request.POST['routes_to']
 routes_name = routes_from+" - "+routes_to
 routes_created_time  = datetime.datetime.now()

 routes = Routes(
      routes_name = routes_name,
      routes_created_time  = routes_created_time
    )
 routes.save()
 return HttpResponseRedirect(reverse('add_route'))

def edit_route(request, id):
  routes_from = request.POST['routes_from']
  routes_to =   request.POST['routes_to']
  routes_name = routes_from+" - "+routes_to
  routes = Routes.objects.get(id=id)
  routes.routes_name = routes_name
  routes.save()
  return HttpResponseRedirect(reverse('index'))


def delete_route(request, id):
  routes = Routes.objects.get(id=id)
  routes.delete()
  return HttpResponseRedirect(reverse('add_route'))


def add_company(request):
   template = loader.get_template('add_company.html') 
   companies = Companies.objects.all().values()
   content = {
   'companies':companies,
   'time':datetime.datetime.now()
   }
   return HttpResponse(template.render(content, request)) 

def insert_company(request):
   companies_name = request.POST['companies_name']
   companies_contact =request.POST['companies_contact']
   companies_office =request.POST['companies_office']
   companies_created_time  = datetime.datetime.now()

   companies = Companies(
    companies_name = companies_name,
    companies_contact = companies_contact,
    companies_office = companies_office,
    companies_created_time  = companies_created_time
    )
   companies.save()
   return HttpResponseRedirect(reverse('add_company'))

def delete_company(request,id):
    companies = Companies.objects.get(id=id)
    companies.delete()
    return HttpResponseRedirect(reverse('add_company'))

def add_region(request):
   template = loader.get_template('add_region.html') 
   regions = Regions.objects.all().values()
   region_value=''
   content = {
      'region_value':region_value,
      'regions':regions,
      'time':datetime.datetime.now()
      }
   if 'edit_region' in request.POST:
     ide=request.POST['id_edit']
     regions = Regions.objects.get(id=ide)
     region_value=regions.regions_name
     content = { 
        'ide':ide,
        'region_value':region_value,
       # 'regions':regions,
        'time':datetime.datetime.now()
     }
     return HttpResponse(template.render(content, request))
   else:
     return HttpResponse(template.render(content, request))
  



def insert_region(request):
 regions_name = request.POST['region_name']
 regions_created_time  = datetime.datetime.now()

 regions = Regions(
      regions_name = regions_name,
      regions_created_time  = regions_created_time
    )
 regions.save()
 return HttpResponseRedirect(reverse('add_region'))

def update_region(request,id):
  regions_name = request.POST['region_name'] 
  regions = Regions.objects.get(id=id) 
  regions.regions_name = regions_name   
  regions.save() 
  return HttpResponseRedirect(reverse('add_region'))


def delete_region(request,id):
  regions = Regions.objects.get(id=id)
  regions.delete()
  return HttpResponseRedirect(reverse('add_region'))