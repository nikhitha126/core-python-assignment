def booking(seat, booked):
    if seat not in booked:
        booked.append(seat)
        return f"Seat {seat} booked successfully!"
    else:
        return f"Seat {seat} is already booked."

def cancelling(seat, booked):
    if seat in booked:
        booked.remove(seat)
        return f"Seat {seat} canceled successfully!"
    else:
        return f"Seat {seat} is not booked."

def available(total, booked):
    avail = []
    for seat in range(1, total + 1):
        if seat not in booked:
            avail.append(seat)
    return avail
total_seats = 10
booked_seats = [2, 5, 7]
booking(3, booked_seats)
available_seats= available(total_seats, booked_seats)
print("Available seats:", available_seats)
cancelling(5, booked_seats)
