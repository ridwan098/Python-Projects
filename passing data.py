def functionb():
    firstname = ridwan
    city = London
    country = England
    return firstname, city, country
functionb()

def functiona():
    firstname, city, country = functionb
    print(firstname)
    print(city)
    print(country)
