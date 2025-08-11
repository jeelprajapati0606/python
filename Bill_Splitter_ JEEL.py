print("welcome to the Bill splitter App!")
print()

# que 1

Bill = float(input("Enter total Bill Amount:"))
People =  int(input("Enter Number of people:"))
Tip_percentage =  int(input("Enter tip percentage(0/5/10/15/20:"))
print()


# que 2

if People <=0:
     print("enter number of people ,ask again:")

if Bill <=0 or Tip_percentage <=0:
    if Tip_percentage <=0:
        print("Error! in Tip_percentage")
     if Bill <=0:
        print("Error! in Bill")
print()


# que 3

Tip_Amount = (Tip_percentage/100)*Bill
Final_Bill = Bill + Tip_Amount
Per_Person = Final_Bill/People

print("Tip Amount:₹",Tip_Amount)
print("Final_Bill:",Final_Bill)
print("Per_Person:",Per_Person)

print()


# que 4

X =str(input("would You like to calculate another bill?(yes/no):"))
while X!="no":
    Bill = float(input("Enter total Bill Amount:"))
    People =  int(input("Enter Number of people:"))
    Tip_percentage =  int(input("Enter tip percentage(0/5/10/15/20:"))
    print()

    if People <=0:
         print("enter number of people ,ask again:")

    if Bill or Tip_percentage <=0:
         if Tip_percentage <=0:
            print("Error! in Tip_percentage")
         if Bill <=0:
            print("Error! in Bill")
    print()
    
    Tip_Amount = (Tip_percentage/100)*Bill
    Final_Bill = Bill + Tip_Amount
    Per_Person = Final_Bill/People

    print("Tip Amount:₹",Tip_Amount)
    print("Final_Bill:",Final_Bill)
    print("Per_Person:",Per_Person)

    print()

    X =str(input("would You like to calculate another bill?(yes/no):"))
    if X=="no":
        break








    
    



