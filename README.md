# Movie Ticket Booking System (PS 47)

**Rungta International Skills University – School of Computer Science and Engineering**
**Bachelor of Technology – Computer Science and Engineering**

## Project Overview

A simple console-based movie ticket booking system written in **Python 3**. The user can book seats, cancel bookings, and view the seat map. All bookings are saved in a file (`bookings.txt`), so they are loaded again every time the program starts.

## Concepts Used

- Lists (2D list for the seat map)
- Seat management
- Functions
- File handling

## Hall Details

- Total seats: **15**
- Rows: **A, B, C** | Seat numbers: **1 to 5** (A1 to C5)
- Ticket price: **Rs. 200 per seat**

## Features

1. **Book** – Book one or more seats for a customer and show the amount payable.
2. **Cancel** – Cancel an existing booking.
3. **Seat Map** – Display the hall (`_` = free, `X` = booked) and the seats left.
4. **Validation** – Rejects invalid seats (e.g. `Z9`) and already booked seats.
5. **File saving** – Bookings are loaded from `bookings.txt` at start and saved after every change.

## How to Run

1. Install Python 3.
2. Keep `main.py` and (optionally) `bookings.txt` in the same folder.
3. Run:

```
python main.py
```

## Menu

```
1. Book
2. Cancel
3. Seat map
```

## Data File Format (`bookings.txt`)

One booking per line: `seat,name`

```
A1,Aman
A2,Neha
A3,Neha
```

## Test Cases

| # | Scenario | Input | Expected Output |
|---|----------|-------|-----------------|
| 1 | Normal input | Book A1 for Aman | Seat A1 booked for Aman. Amount: 200 |
| 2 | Boundary | All seats except C5 booked; book C5 for Riya | Seat C5 booked for Riya. Amount: 200. Seats left: 0. Show is now housefull. |
| 3 | Invalid input | (a) Book A1 again (b) Book Z9 | (a) Seat A1 is already booked. (b) Invalid seat. Rows are A to C and seat numbers are 1 to 5. |
| 4 | Different valid scenario | A1 booked by Aman; book A2 and A3 for Neha; view seat map | Seats A2, A3 booked for Neha. Amount: 400. Row A: X X X _ _, Row B: _ _ _ _ _, Row C: _ _ _ _ _, Seats left: 12 |




## Difficulties Faced

1. **Understanding the seat map as a 2D list** – It was confusing at first to convert a seat like `A1` into list positions. Solved by using the row letter to find the row index (`A = 0, B = 1, C = 2`) and `seat number - 1` as the column index.
2. **Validating seat input** – Inputs like `Z9`, `A6`, or an empty entry caused errors. Solved by checking the length, the row letter (A to C) and the seat number (1 to 5) before using the seat.
3. **Preventing double booking** – Had to make sure an already booked seat cannot be booked again. Solved by checking the seat map before booking and showing the message "Seat is already booked."
4. **Booking multiple seats in one go (Test Case 4)** – Booking A2 and A3 for Neha and calculating the amount (2 x 200 = 400) needed care. Solved by looping over each seat and multiplying the number of booked seats by the ticket price.
5. **File handling** – Making sure bookings are saved after every change and loaded properly when the program restarts. Faced issues with missing files on the first run and extra blank lines. Solved by handling the "file not found" case and stripping each line while reading.
6. **Cancelling a booking** – After cancelling, the seat map and `bookings.txt` both had to be updated. Solved by rewriting the whole file after each change.
7. **Matching the exact expected output** – Small differences in spacing or wording failed the test cases, so the output format was adjusted carefully to match the given format.

## What I Learned

- How to use 2D lists for real-life problems
- Writing small reusable functions
- Reading from and writing to files
- Input validation and testing with different cases

## Project Structure

```
movie-ticket-booking/
├── main.py
├── bookings.txt
└── README.md
```

## Author

Name: Anish Ranjan
Roll No.: Ru-26-00537
Course: B.Tech CSE, Rungta International Skills University
