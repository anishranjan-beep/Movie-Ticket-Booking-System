
PRICE = 200
FILE_NAME = "bookings.txt"

# Create 3 rows with 5 seats each
seats = {
    "A": [None] * 5,
    "B": [None] * 5,
    "C": [None] * 5
}


# Load previous bookings
def load_bookings():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                seat, name = line.strip().split(",", 1)
                row = seat[0]
                number = int(seat[1:]) - 1

                if row in seats and 0 <= number < 5:
                    seats[row][number] = name

    except FileNotFoundError:
        pass


# Save bookings
def save_bookings():
    with open(FILE_NAME, "w") as file:
        for row in seats:
            for i in range(5):
                if seats[row][i] is not None:
                    file.write(f"{row}{i+1},{seats[row][i]}\n")


# Show seat map
def show_seats():
    print("\n--- SEAT MAP ---")

    for row in seats:
        status = []

        for seat in seats[row]:
            if seat is None:
                status.append("_")
            else:
                status.append("X")

        print("Row", row + ":", " ".join(status))

    left = 0

    for row in seats:
        left += seats[row].count(None)

    print("Seats left:", left)

    if left == 0:
        print("Show is now housefull.")


# Book seats
def book_seat():
    seat_input = input("Enter seat(s): ").upper().split(" ")

    # Check for empty input and duplicate seats
    if not seat_input or len(seat_input) != len(set(seat_input)):
        print("Invalid seat.")
        return

    selected = []

    # Validate all seats before booking
    for seat in seat_input:

        if len(seat) < 2:
            print("Invalid seat.")
            return

        row = seat[0]
        number = seat[1:]

        if row not in seats or not number.isdigit():
            print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
            return

        number = int(number)

        if number < 1 or number > 5:
            print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
            return

        if seats[row][number - 1] is not None:
            print("Seat", seat, "is already booked.")
            return

        selected.append((row, number - 1, seat))

    name = input("Enter name: ")

    # Book all selected seats
    for row, number, seat in selected:
        seats[row][number] = name

    save_bookings()

    amount = len(selected) * PRICE

    if len(selected) == 1:
        print("Seat", selected[0][2], "booked for", name,
              "Amount:", amount)
    else:
        seat_names = ", ".join(item[2] for item in selected)
        print("Seats", seat_names, "booked for", name,
              "Amount:", amount)

    show_seats()


# Cancel booking
def cancel_seat():
    seat = input("Enter seat to cancel: ").upper()

    if (len(seat) < 2 or seat[0] not in seats
            or not seat[1:].isdigit()
            or not 1 <= int(seat[1:]) <= 5):
        print("Invalid seat.")
        return

    row = seat[0]
    number = int(seat[1:]) - 1

    if seats[row][number] is None:
        print("Seat is not booked.")
    else:
        seats[row][number] = None
        save_bookings()
        print("Booking cancelled for seat", seat)


# Main program
load_bookings()

while True:
    print("\n--- MOVIE TICKET BOOKING SYSTEM ---")
    print("1. Book")
    print("2. Cancel")
    print("3. Seat map")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_seat()

    elif choice == "2":
        cancel_seat()

    elif choice == "3":
        show_seats()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
