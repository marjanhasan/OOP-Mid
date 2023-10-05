class Star_Cinema:
    hall_list = []

    def __init__(self) -> None:
        pass

    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = ()
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
