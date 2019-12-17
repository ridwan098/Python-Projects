# Tipper program where the user enters a restaurant bill total. The program will then display two amounts; a 15 percent tip and 20 percent tip.

Bill = float(input("Enter your bill total: "))
total1 = Bill * 0.15
total2 = Bill * 0.2
print("The 15 percent tip is:" , total1)
print("The 20 percent tip is:" , total2)
