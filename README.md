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
class :section k
