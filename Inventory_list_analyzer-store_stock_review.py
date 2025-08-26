
print("Welcome to Inventory List Analyzer !")
print()

l=[]

while True:
    item =input("Enter item name:")
    category =input("Enter category:")
    quantity =int(input("Enter Quantity:"))
    add =input("Do you want to add more items? (y/n):")

l.append({
        "Item": item,
        "Category": category,
        "Quantity": quantity,
        "Add": add
    })
print()


for i in l:
     if l[3] == 'y' or 'yes':
        print (i)
        print()













