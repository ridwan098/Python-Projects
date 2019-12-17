class Tuna:
    name = ""
    def __init__(self, object):
        print("im a fish")
        self.name = object
        print("My name is " + self.name)

    def swim(self):
        print("I am swimming")


fl = Tuna("dsafs")
fl.swim()
