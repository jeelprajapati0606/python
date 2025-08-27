
print("Welcome to Inventory list Analyzer!")
print()

l = []

while True:
    item = input("Enter item name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))

    l.append({
        "Item": item,
        "Category": category,
        "quantity": quantity
    })
    print()
    add = input("Do you want to add more items? (y/n): ")
    print()

    if add.lower() in ("n", "no"):
        print()   
        break
    

print("========= Inventory Summary ===========")

print()

# Total items

total_items = len(l)
item_names = [i["Item"] for i in l]
print("Total Different Items: " ,total_items)
print("Explanation: You entered " ,total_items, " different items: " , ", ".join(item_names))


# Total quantity

print()

quantities = [i["quantity"] for i in l]
total_quantity = sum(quantities)
print("Total quantity in Stock: " ,total_quantity)
print("Explanation: Sum of all quantities: " , " + ".join(str(q) for q in quantities) , " = " ,total_quantity)


# Average

print()

average_quantity = total_quantity / total_items
print("Average Quantity per Item: " , round(average_quantity, 2))
print("Explanation: Average = " , total_quantity , " total / " , total_items , " items")


# Most stocked item

print()

most_stocked = l[0]
least_stocked = l[0]


for i in l:
    if i["quantity"] > most_stocked["quantity"]:
        most_stocked = i
    if i["quantity"] < least_stocked["quantity"]:
        least_stocked = i

print("Most Stocked Item: " , most_stocked["Item"] ," (" ,most_stocked["quantity"] , " units)")
print("Explanation: " , most_stocked["Item"] , " has the highest quantity among all items.")

print()

print("Least Stocked Item: " , least_stocked["Item"] , " (" ,least_stocked["quantity"] , " units)")
print("Explanation: " , least_stocked["Item"] , " has the lowest quantity.")

print()

# Categories
print("----------------------------------\n")
unique_categories = sorted(set(i["Category"] for i in l))

print("Unique Categories in Inventory: " + str(unique_categories))
print("Explanation: Categories are taken from user input and converted to lowercase.")
print("No duplicates are shown here.")

print()

#  Items sorted by quantity (descending)
print("----------------------------------")

print()

print("📦 Items Sorted by Quantity (High to Low):\n")

sorted_items = sorted(l, key=lambda x: x["quantity"], reverse=True)
count = 1                                                                             # doubt
for i in sorted_items:
    print(str(count) + ". " + i["Item"] + " - " + str(i["quantity"]) + " units")
    count += 1

print("\nExplanation: Items are sorted using the quantity field from highest to lowest.")

print()

# Categories in alphabetical order
print("----------------------------------")

print()

print("📂 Categories in Alphabetical Order:")

categories = sorted(set(i["Category"] for i in l))
count = 1
for c in categories:
    print(str(count) , ". " , c)
    count += 1

print("Explanation: The set of unique categories was sorted alphabetically for display.")

print()

print("=========== END OF REPORT ===========")








    










            




     

















