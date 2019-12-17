class Parent():

    def print_last_name(self):
        print("Gbadamosi")


class Child(Parent):

    def print_first_name(self):
        print("Ridwan")

    def print_last_name(self):
        print("Ishola")

ridwan = Child()

ridwan.print_first_name()
ridwan.print_last_name()
