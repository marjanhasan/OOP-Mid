class Star_Cinema:
    _hall_list = []

    def __init__(self) -> None:
        pass

    def _entry_hall(self, hall):
        self._hall_list.append(hall)

    def __repr__(self) -> str:
        for hall in self._hall_list:
            print(f"Hall Number: {hall._hall_no}")
            print(f"Rows: {hall._rows}, Columns: {hall._cols}")

            print("\nAvailabe Shows are down below")
            for show in hall._show_list:
                print(f"Show ID: {show[0]}, Name: {show[1]}, Time: {show[2]}")

            print("\nAvailabe seats are down below")

            for show_id, seat_arrangement in hall._seats.items():
                print(f"Available seats for show id: {show_id}")

                for row in seat_arrangement:
                    print(" ".join(map(str, row)))
                print()

            print()
        return f"Welcome for the best ever 5* experiences\n"


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        super().__init__()
        self._entry_hall(self)

    def _entry_show(self, id, movie_name, time):
        if len(self._show_list) == 0:
            show = (id, movie_name, time)
            self._show_list.append(show)

            seat = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
            self._seats[id] = seat
            return

        for show in self._show_list:
            if show[0] == id:
                print(f"Show ID '{id}' already exists.")
                return

        show = (id, movie_name, time)
        self._show_list.append(show)

        seat = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[id] = seat

    def _book_seats(self, id, bookings):
        if id in self._seats:
            for book in bookings:
                row = int(book[0])
                col = int(book[1])

                if (row < 0) or (self._rows <= row) or (col < 0) or (self._cols <= col):
                    print(f"\nInvalid seat position ({row}, {col}). Please try again!")
                    continue

                if self._seats[id][row][col] == 0:
                    self._seats[id][row][col] = 1
                    print(
                        f"\nSeat ({row}, {col}) is booked successfully for the show ID {id}"
                    )

                else:
                    print(
                        f"\nSeat ({row}, {col}) is already booked for the show ID {id}. Please try again!"
                    )

        else:
            print(f"\nInvalid show ID: {id}. Please try again!")

    def _view_show_list(self):
        if len(self._show_list) != 0:
            print("\nAvailabe Shows are down below")

            for show in self._show_list:
                print(f"\nShow ID: {show[0]}, Name: {show[1]}, Time: {show[2]}")

        else:
            print("\nOops! There are no available shows today.")

    def _view_available_seats(self, id):
        if len(self._show_list) == 0:
            print("\nOops! There are no available shows today.")
            return

        if id in self._seats:
            print("\nAvailabe seats are down below")

            for row in self._seats[id]:
                for element in row:
                    print(element, end=" ")
                print()

        else:
            print(f"\nOops! Invalid show ID: {id}. Please try again")

    def __repr__(self) -> str:
        print("\nAvailabe Shows are down below")

        for show in self._show_list:
            print(f"Show ID: {show[0]}, Name: {show[1]}, Time: {show[2]}")

        print("\nAvailabe seats are down below")

        for show_id, seat_arrangement in self._seats.items():
            print(f"Available seats for show id: {show_id}")

            for row in seat_arrangement:
                print(" ".join(map(str, row)))
            print()

        return f"Welcome for the best ever 5* experiences\n"


hall1 = Hall(6, 6, 1)
hall1._entry_show("111", "Jawan", "6/10/23 10:00AM")
hall1._entry_show("112", "Barbie", "6/10/23 12:00PM")
hall1._entry_show("113", "Oppenheimer", "6/10/23 2:00PM")

while True:
    print("\nOptions:\n")
    print("1: Today's available show")
    print("2: Show available seats")
    print("3: Book Seats")
    print("4: Exit")

    ch = int(input("\nEnter Options: "))

    if ch == 1:
        hall1._view_show_list()

    elif ch == 2:
        id = input("Please Enter show ID: ")
        hall1._view_available_seats(id)

    elif ch == 3:
        id = input("Please Enter show ID: ")
        seats = int(input("How many seats do you want (in number): "))

        if seats == 0:
            print("\nInvalid seats", seats, "Please try again!")
            continue

        bookings = []

        while seats != 0:
            print("Please Enter your seats like (row, column) separately asked")
            row = input("Please enter row: ")
            col = input("Please enter col: ")
            bookings.append((row, col))
            seats -= 1

        hall1._book_seats(id, bookings)

    elif ch == 4:
        break

    else:
        print("\nOops Invalid options. Please select between 1, 2, 3 or 4")
