cars = 100
drivers = 40
passengers = 90
space_in_a_car = 4.0
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "there are",cars,"cars available."
print "there are only ",drivers,"drivers available."
