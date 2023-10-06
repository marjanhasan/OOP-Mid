class Star_Cinema:
    _hall_list = []

    def __init__(self) -> None:
        pass

    @classmethod
    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self._hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        if len(self.__show_list) == 0:
            show = (id, movie_name, time)
            self.__show_list.append(show)
            seat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
            self.__seats[id] = seat
            return
        for show in self.__show_list:
            if show[0] == id:
                print(f"Show ID '{id}' already exists.")
                return
        show = (id, movie_name, time)
        self.__show_list.append(show)
        seat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.__seats[id] = seat

    def book_seats(self, id, bookings):
        if id in self.__seats:
            for book in bookings:
                row = int(book[0])
                col = int(book[1])
                if (row < 0) or (self.rows <= row) or (col < 0) or (self.cols <= col):
                    print(f"\nInvalid seat position ({row}, {col}). Please try again!")
                    continue
                if self.__seats[id][row][col] == 0:
                    self.__seats[id][row][col] = 1
                    print(
                        f"\nSeat ({row}, {col}) is booked sucessfully for the show ID {id}"
                    )
                else:
                    print(
                        f"\nSeat ({row}, {col}) is already booked for the show ID {id}"
                    )

        else:
            print(f"\nInvalid show ID: {id}. Please try again!")

    def view_show_list(self):
        if len(self.__show_list) != 0:
            print("\nAvailabe Shows are down below")
            for show in self.__show_list:
                print(f"\nShow ID: {show[0]}, Name: {show[1]}, Time: {show[2]}")
        else:
            print("\nOops! There are no available shows today.")

    def view_available_seats(self, id):
        if len(self.__show_list) == 0:
            print("\nOops! There are no available shows today.")
            return
        if id in self.__seats:
            print("\nAvailabe seats are down below")
            for row in self.__seats[id]:
                for element in row:
                    print(element, end=" ")
                print()
        else:
            print(f"\nOops! Invalid show ID: {id}. Please try again")

    def __repr__(self) -> str:
        print("\nAvailabe Shows are down below")
        for show in self.__show_list:
            print(f"Show ID: {show[0]}, Name: {show[1]}, Time: {show[2]}")
        print("\nAvailabe seats are down below")
        for show_id, seat_arrangement in self.__seats.items():
            print(f"Available seats for show id: {show_id}")
            for row in seat_arrangement:
                print(" ".join(map(str, row)))
            print()
        return f"Welcome for the best ever 5* experiences\n"


banalata = Hall(6, 6, 2)
banalata.entry_show("111", "Jawan", "6/10/23 10:00AM")
banalata.entry_show("112", "Barbie", "6/10/23 12:00PM")
banalata.entry_show("113", "Oppenheimer", "6/10/23 2:00PM")
while True:
    print(banalata)

    print("Options:\n")
    print("1: Book Seats")
    print("2: Entry Show")
    print("3: Exit")

    ch = int(input("\nEnter Options: "))

    if ch == 1:
        id = input("Please Enter show ID: ")
        seats = int(input("How many seats do you want (in number): "))
        bookings = []
        while seats != 0:
            print("Please Enter your seats like (row, column) separately asked")
            row = input("Please enter row: ")
            col = input("Please enter col: ")
            bookings.append((row, col))
            seats -= 1
        banalata.book_seats(id, bookings)
    elif ch == 2:
        id = input("Please Enter show ID: ")
        movie_name = input("Please enter show name: ")
        time = input("Please enter show time: ")
        banalata.entry_show(id, movie_name, time)
    elif ch == 3:
        break
    else:
        print("\nOops Invalid options. Please select between 1,2 or 3")
