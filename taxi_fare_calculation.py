def calculate(distance):
    return 50 + (10 * distance)
trips = [5, 10, 3]  #distance in km
total = 0
for i, dist in enumerate(trips, 1):
    fare = calculate(dist)
    total += fare
    print(f"Trip {i}: ${fare}")
print(f"Total Fare: ${total}")
