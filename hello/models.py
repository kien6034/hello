from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    #if delete the airpot, delete the corresponding flight as well
    #if have an airpot, and want to access a flight whose has the origin is that airpot,
    #we can use related_names to access that
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name= "departures") 
    destination = models.ForeignKey(Airport, on_delete= models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def is_valid_flight(self):
        return (self.origin != self.destination) and (self.duration >= 0)

    #define what objects should look like when being printed out on the screen
    def __str__(self):
        return f"{self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank = True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
    