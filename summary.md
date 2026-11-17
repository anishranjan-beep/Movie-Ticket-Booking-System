# Movie Ticket Booking System — Project Summary

## 1. Introduction

The **Movie Ticket Booking System** is a console-based application developed using Python 3. It manages movie seat reservations in a small cinema hall. Users can book seats, cancel bookings, view the seat map, and check the ticket amount. Booking details are stored in a text file so they can be loaded when the program starts again.

## 2. Project Details

| Item | Details |
|---|---|
| Project title | Movie Ticket Booking System |
| PS No. | 47 |
| Programming language | Python 3 |
| Application type | Console-based |
| Hall capacity | 15 seats |
| Seat arrangement | 3 rows (A, B, C), with 5 seats in each row |
| Seat labels | A1–A5, B1–B5, and C1–C5 |
| Ticket price | Rs. 200 per seat |
| Booking data file | `bookings.txt` |

## 3. Objectives

- Create and display a seat map for a 15-seat movie hall.
- Allow users to book an available seat using its seat code and customer name.
- Prevent an already-booked seat from being booked again.
- Allow users to cancel an existing booking.
- Calculate the ticket amount at Rs. 200 per seat.
- Save booking details in a file and load them when the program starts.
- Display the number of available seats and indicate when the hall is full.

## 4. Main Features

- **Book a seat:** Accepts a seat code and customer name, checks that the seat is valid and available, and records the booking.
- **Cancel a booking:** Removes an existing reservation so the seat becomes available again.
- **View seat map:** Displays the status of seats in rows A, B, and C.
- **Calculate amount:** Calculates the ticket cost at Rs. 200 per seat.
- **File handling:** Uses `bookings.txt` to save and reload booking details.
- **Seat availability:** Tracks the number of unbooked seats and identifies when the hall is full.

## 5. Python Concepts Used

- **Lists / 2D list:** Represents the three rows and five seats in each row.
- **Functions:** Separates tasks such as booking, cancellation, displaying seats, loading, and saving.
- **Conditional statements:** Validate seat codes and check booking status.
- **Loops:** Process rows, seats, and booking records.
- **File handling:** Reads from and writes to `bookings.txt`.
- **Exception handling:** Can handle cases such as the booking file not existing when the program starts.

## 6. Program Workflow

1. Start the program and initialize all 15 seats as available.
2. Load previously saved bookings from `bookings.txt`.
3. Display the menu: Book, Cancel, or Seat Map (and an exit option if included in the implementation).
4. Perform the selected operation after validating the user's input.
5. Update the seat information and save the changed bookings to the file.
6. Display the updated seat map and available-seat count when requested.

## 7. Test Cases from the Problem Statement

### Test Case 1 — Normal Input

**Input:** Choose Book; enter seat `A1` and name `Aman`.

**Expected output:** Seat A1 is booked for Aman. Amount: Rs. 200.

### Test Case 2 — Boundary / Minimum Input

**Input:** All seats except `C5` are booked; choose Book; enter `C5` and name `Riya`.

**Expected output:** Seat C5 is booked for Riya; seats left: 0; the system reports that the hall is full.

### Test Case 3 — Invalid Input

**Input:** Try to book `A1` when it is already booked; then enter the invalid seat code `Z9`.

**Expected output:** The program reports that A1 is already booked and rejects Z9 because valid rows are A to C and seat numbers are 1 to 5.

### Test Case 4 — Different Valid Scenario

**Input:** A1 is booked by Aman; book A2 and A3 for Neha; select the seat-map option.

**Expected output:** A2 and A3 are booked for Neha. Amount: Rs. 400. The seat map shows the occupied seats and 12 seats left.
## Difficulties Faced

1. **Booking more than one seat at once (Test Case 4).**
At first the program treated the whole input, such as `A2 and A3`, as a single seat, so it printed "Invalid seat". It also failed on `c4 c5`.
*Solution:* the input is converted to uppercase, commas and the word `and` are replaced with spaces, and `split()` turns it into a list of seats. Each seat is then validated and booked one by one.
2. **Handling a mix of valid and invalid seats in one input.**
If one seat in the list was invalid or already booked, the other seats still had to be handled correctly.
*Solution:* every seat is checked separately. Only the valid, free seats are booked, and an error message is printed for each bad one.
3. **Calculating the correct amount.**
The amount had to change with the number of seats booked, not just show a fixed Rs. 200.
*Solution:* the amount is calculated as the number of seats actually booked multiplied by the ticket price, so two seats give Rs. 400.
4. **Preventing double booking.**
A seat that is already booked must never be booked again.
*Solution:* booked seats are stored in a dictionary (seat to name), and each seat is checked against it before booking.
5. **Keeping bookings after the program closes.**
The seat map has to be the same the next time the program is run.
*Solution:* bookings are written to `bookings.txt` after every booking or cancellation and loaded again when the program starts.
6. **Showing the seat map and the seats left correctly.**
The map had to show `X` for booked seats and `\_` for free ones, with the right count of seats left (12 in Test Case 4).
*Solution:* the map is built with nested loops over rows A to C and seats 1 to 5, and seats left is calculated as 15 minus the number of booked seats.
7. **Matching the exact expected output of each test case.**
The messages had to match the expected output, for example "Seats A2, A3 booked for Neha" for two seats and "Seat A1 booked for Aman" for one.
*Solution:* the program checks how many seats were booked and uses "Seat" or "Seats" to suit, and it prints the housefull message when no seats are left.

## 8. Possible Difficulties and Learning Outcomes

The problem statement does not specify the difficulties actually encountered during development. The following are likely implementation challenges based on the required features. Edit this section to reflect the issues experienced while developing and testing the program.

- Representing the hall correctly as three rows with five seats each.
- Validating seat codes such as A1 to C5 and rejecting invalid entries.
- Checking whether a seat is already booked before accepting a new booking.
- Keeping the seat map, available-seat count, and booking records consistent after booking or cancellation.
- Reading and writing booking details correctly in `bookings.txt`.
- Handling the first program run when no booking file exists yet.

## 9. Conclusion

The Movie Ticket Booking System demonstrates how basic Python programming concepts can be combined to build a useful console application. It provides seat management, booking and cancellation operations, ticket-cost calculation, seat-map display, and file-based data storage. The project helps develop practical understanding of lists, functions, loops, conditions, input validation, and file handling.

---

*End of Project Summary*
