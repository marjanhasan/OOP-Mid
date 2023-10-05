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
        if id not in self.seats:
            show = (id, movie_name, time)
            self.show_list.append(show)
            seat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
            self.seats[id] = seat
        else:
            print(f"Show ID '{id}' already exists.")

    def book_seats(self, id, bookings):  # todo bookings list
        if id not in self.seats:
            if 0 <= self.rows and 0 <= self.cols:
                if self.seats[id][self.rows][self.cols] == 0:
                    self.seats[id][self.rows][self.cols] = 1
                    print(f"Seat ({self.rows}, {self.cols} is booked for show ID {id})")
                else:
                    print(
                        f"Seat ({self.rows}, {self.cols}) is already booked for show ID {id}"
                    )
            else:
                print(f"Invalid seat position. Please try again!")
        else:
            print(f"Invalid show ID. Please try again!")

    def view_show_list(self):
        if 0 != len(self.show_list):
            print("Availabe Shows are down below")
            for show in self.show_list:
                print(show)
        else:
            print("Oops! There are no available shows today.")

    def view_available_seats(self, id):
        if id in self.seats:
            for row in self.seats[id]:
                print(row)
        else:
            print(f"There is not availble seats on show ID {id}")
