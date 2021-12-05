from observerInterfaces import Observer, Subject


class Manager(Observer):
    def update(self, subject: Subject, num: int) -> None:
        if num == 20:
            self.update_x(subject)
        elif num == 100:
            self.update_y(subject)

    @staticmethod
    def update_x(subject: Subject) -> None:
        inp: str = input("Do you want to print out X receipt: (y/n)")
        if inp == "y":
            subject.print_x_report()

    @staticmethod
    def update_y(subject: Subject) -> None:
        inp: str = input("Do you want to end shift: (y/n)")
        if inp == "y":
            subject.close_cashier()
