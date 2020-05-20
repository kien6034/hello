from django.shortcuts import render

# Create your views here.
from django.http import  Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

def home(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk = flight_id) # pk: primary key
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")

    context = {
        "flight": flight,
        "non_passengers": flight.passengers.all(), # get passenger from flight object
        "passengers": Passenger.objects.exclude(flights=flight).all()  
        #get rid of all the passengers have this particualr "flight" in their list of flights
    }
    return render(request, "flights/flight.html", context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"]) 
        passenger = Passenger.objects.get(pk = passenger_id)
        flight = Flight.objects.get(pk = flight_id)
    except KeyError:
        return render(request, "flights/error.html", {"message": "No selection"})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No flight"})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No passenger"})

    passenger.flights.add(flight)  # from that passenger, go to flights, and add that flight
    # knowing the name of the route you want to go to, you use "reverse"
    # normal way is going to the fucntion, but using reverse means that you know the name of the function 
    # and you want to access the url associated with that function 
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))  # flight is the name of the url
