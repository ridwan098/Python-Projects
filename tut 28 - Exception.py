import traceback

while True:
    try:
        number = int(input("what us your favour number? \n"))
        print(number/18)
        break
    except NameError:
        print("Dont enter a letter or words")
    finally:
        print("loop complete")



