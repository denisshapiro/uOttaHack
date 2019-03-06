# Rento

Allows users to input their current location as an address through SMS. Using [Twilio](https://www.twilio.com/), returns the nearest available vehicle that can be rented. 

Users can access a map of all available vehicles through the website. The distance between the user's location and locations of the closest cars is calculated with the Haversine Formula. Latitude and longitude's extracted using [Google Maps API](https://cloud.google.com/maps-platform/).

Since internet access can be difficult while on the move, it is possible for users to input their current location as an address through SMS which then compares the user's location to the location of cars stored in a database. The address of the car nearest to the user is sent through SMS, as well as the car's make and model. The user can then text that they have reserved that car which makes it invisible to others, allowing the user to go to the car's location and start driving. When the car is done being driven, the user can unreserve the car through SMS, and others can then see it and reserve it.
