class Female:
    gender = "female"

    def __init__(self, name, age):
        self.name = name
        self.age = age


r = Female("rachel", 16)
l = Female("leah", 21)

print(r.gender)
print(r.name)
print(str(r.age) + "\n")

print(l.gender)
print(l.name)
print(str(l.age) + "\n")

