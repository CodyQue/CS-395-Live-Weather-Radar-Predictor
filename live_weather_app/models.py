from django.db import models

# Model used for storing information of places in SQLite database
class Place(models.Model): 
    name = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length = 20)
    temperature = models.CharField(max_length = 20)
    wind = models.CharField(max_length = 20)
    humidity =models.CharField(max_length = 20)
    iconWeb = models.CharField(max_length=100, default = "https://openweathermap.org/img/wn/10d@2x.png")
    lat = models.CharField(max_length = 20, default = "40")
    long = models.CharField(max_length = 20, default = "-74")

    def __str__ (self):
        return f"Name: {self.name}, Description: {self.description}, Temperature: {self.temperature}, Wind: { self.wind }, Humidity: { self.humidity}, Icon: { self.iconWeb}, Lat: {self.lat}, Long: {self.long}"