from enum import Enum, auto
from Booking import Luxury


class Type(Enum):
    INT = auto()
    BOOL = auto()
    STRING = auto()


class BookingCLI:
    INSTR: list[str] = [
        "1 to add new booking",
        "2 to search existing booking",
        "3 to list all bookings",
        "4 to update a booking",
        "5 to remove a booking",
        "Enter any other key to quit",
    ]
    bookings: list[Luxury]

    def __init__(self) -> None:
        self.bookings = []
        self.__cli()

    def __cli(self) -> None:
        CMD: int = int(input(f"{self.__linebreak()}\n{', '.join(self.INSTR)}\n"))
        match CMD:
            case 1:
                self.bookings = [*self.bookings, self.__new()]
            case 2:
                print(self.__search())
            case 3:
                print(self.__list())
            case 4:
                self.bookings = self.__update()
            case 5:
                self.bookings = self.__remove()
            case _:
                exit(0)
        self.__cli()

    def __linebreak(self) -> str:
        """Function that creates a string linebreak"""
        return "__________"

    def __new(self) -> Luxury:
        """Creates a new Luxury object"""
        return Luxury(
            self.__validate("Enter Booking ID: "),
            self.__validate("Enter Booking Date: "),
            self.__validate("Enter Number of Weeks: ", Type.INT),
            self.__validate("Enter Property Owner Name: "),
            self.__validate("Enter Contact Number: "),
            self.__validate("Enter Booking Address: "),
            self.__validate("Enter Number of Rooms: ", Type.INT),
            self.__validate("Enter Garden Area: ", Type.INT),
            self.__validate("Perform Alarm Check? (Y/N): ", Type.BOOL),
            self.__validate("Perform Pool Upkeep? (Y/N): ", Type.BOOL),
        )

    def __validate(self, MSG: str, T: Type = Type.STRING) -> str | int | bool:
        """Validate user input for new Luxury Objects"""
        out: str | int | bool
        flag: bool = False
        while flag is False:
            out = input(MSG)
            match T:
                case Type.INT:
                    if out is not None and out != "":
                        try:
                            out = int(out)
                            flag = True
                        except ValueError:
                            continue
                case Type.BOOL:
                    if out is not None and out.upper() in ["Y", "N"]:
                        out = True if out.upper() == "Y" else False
                        flag = True
                case Type.STRING:
                    if out is not None and out != "":
                        flag = True
        return out

    def __search(self) -> Luxury | str:
        """Finds the Luxury object from the bookings list"""
        ID: str = input("Enter Booking ID to search: ")
        for booking in self.bookings:
            if ID == booking.get_booking_id():
                return booking
        return "Invalid Booking ID!"

    def __list(self) -> str:
        """Returns all Luxury objects as a string"""
        return "\n".join(booking.__str__() for booking in self.bookings)

    def __update(self) -> list[Luxury]:
        """Updates an existing Luxury in the bookings list"""
        ID: str = input("Enter Booking ID to update: ")
        for i, booking in enumerate(self.bookings):
            if ID == booking.get_booking_id():
                self.bookings[i] = self.__new()
        return self.bookings

    def __remove(self) -> list[Luxury]:
        """Remove a Luxury from the bookings list"""
        ID: str = input("Enter Booking ID to remove: ")
        return [booking for booking in self.bookings if booking.get_booking_id() != ID]


if __name__ == "__main__":
    BookingCLI()
