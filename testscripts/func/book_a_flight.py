def book_flight(departure_city, destination_city, seat,/, date="2025-12-14", return_date=None, *, travel_class="economy"):
    print(f"\nBooking flight: \nFrom - {departure_city}. \nTo - {destination_city}. \nSeat - {seat}. \nOn - {date}. \nReturn on - {return_date}")
    booking_details={
        "departure_city": departure_city,
        "destination_city": destination_city,
        "date": date,
        "return_date": return_date,
        "seat": seat,
        "travel_class": travel_class
    }
    print(f"Booking Details: {booking_details}")

book_flight("New York", "London", "12A", date="2025-12-20", return_date="2026-01-05", travel_class="business")
book_flight(departure_city="Tel Aviv", destination_city="Paris", seat="7B", date="2025-11-15", travel_class="first")