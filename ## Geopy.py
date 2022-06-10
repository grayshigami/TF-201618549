## Geopy
from geopy.geocoders import Nominatim 
geolocator = Nominatim(user_agent="uber")

## 0
location = geolocator.geocode("Luis Aldana, 15034, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 1 
location = geolocator.geocode("Del Lenguaje, 102, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 2
location = geolocator.geocode("Del Lenguaje, 182, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 3
location = geolocator.geocode("Avenida del Aire , 283, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 4
location = geolocator.geocode("Avenida del Aire, 15034, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 5
location = geolocator.geocode("Calle de las Letras, 103, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 6
location = geolocator.geocode("Boulevard de la Literatura, 15034, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 7
location = geolocator.geocode("Avenida Javier Prado Este, 15034, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

##8
location = geolocator.geocode("Av. Javier Prado Este , 1797-1633, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

##9
location = geolocator.geocode("Jr cuzco , 264, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

##10
location = geolocator.geocode("Avenida Del Aire , 380, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 11
location = geolocator.geocode("Av. De La Poesía , 356-398, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 12 
location = geolocator.geocode("WX7V+MJM, Avenida De La Poesía, 15034, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 13
location = geolocator.geocode("Calle de las Letras , 269-285, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 14
location = geolocator.geocode("Luis Aldana, 15034, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 15
location = geolocator.geocode("Torres De San Borja, 15034, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 16
location = geolocator.geocode("Calle de Las Musas , 147-101, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 17
location = geolocator.geocode("Calle de las Letras , 395, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 18
location = geolocator.geocode("Calle de Las Musas , 291, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 19
location = geolocator.geocode("Avenida Aviación , 2204, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 

## 20
location = geolocator.geocode("Avenida Aviación , 2346, San Borja") 
print(location.address)
print((location.latitude, location.longitude)) 
