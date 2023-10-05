class Star_Cinema:
    hall_list = []

    def __init__(self) -> None:
        pass

    @classmethod
    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        if len(self.show_list) == 0:
            show = (id, movie_name, time)
            self.show_list.append(show)
            seat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
            self.seats[id] = seat
            return
        for show in self.show_list:
            if show[0] == id:
                print(f"Show ID '{id}' already exists.")
                return
        show = (id, movie_name, time)
        self.show_list.append(show)
        seat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seat

    def book_seats(self, id, bookings):
        if id in self.seats:
            for book in bookings:
                row = int(book[0])
                col = int(book[1])
                if (row < 0) or (self.rows <= row) or (col < 0) or (self.cols <= col):
                    print(f"Invalid seat position ({row}, {col}). Please try again!")
                    continue
                if self.seats[id][row][col] == 0:
                    self.seats[id][row][col] = 1
                    print(
                        f"Seat ({row}, {col}) is booked sucessfully for the show ID {id}"
                    )
                else:
                    print(f"Seat ({row}, {col}) is already booked for the show ID {id}")

        else:
            print(f"Invalid show ID: {id}. Please try again!")

    def view_show_list(self):
        if len(self.show_list) != 0:
            print("Availabe Shows are down below")
            for show in self.show_list:
                print(f"Show ID: {show[0]}, Name: {show[1]}, Time: {show[2]}")
        else:
            print("Oops! There are no available shows today.")

    def view_available_seats(self, id):
        if len(self.show_list) == 0:
            print("Oops! There are no available shows today.")
            return
        if id in self.seats:
            print("Availabe seats are down below")
            for row in self.seats[id]:
                for element in row:
                    print(element, end=" ")
                print()
        else:
            print(f"Oops! Invalid show ID: {id}. Please try again")

    def __repr__(self) -> str:
        print("\nAvailabe Shows are down below")
        for show in self.show_list:
            print(f"Show ID: {show[0]}, Name: {show[1]}, Time: {show[2]}")
        print("\nAvailabe seats are down below")
        for show_id, seat_arrangement in self.seats.items():
            print(f"Available seats for show id: {show_id}")
            for row in seat_arrangement:
                print(" ".join(map(str, row)))
            print()
        return f"Welcome for the best ever 5* experiences\n"


banalata = Hall(6, 6, 2)
banalata.entry_show("111", "Jawan", "6/10/23 10:00AM")
banalata.entry_show("112", "Dhawan", "6/10/23 12:00PM")
banalata.book_seats("111", [(0, 0), (0, 1)])
t = 3
while t != 0:
    print(banalata)
    t -= 1
