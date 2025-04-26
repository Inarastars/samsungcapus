#создать библиотеку с данными о давтде дой
#dic_person = {
#    "Last name" : "Doe",
#    "First name" : "David",
#    "Company" : "Samsung"
#}
#for key in dic_person:
#    print(f"{key:<11}: {dic_person[key]}")

#магазин, с списком колва предметов
#items = {
#    "Coffee" : 7,
#    "Pen" : 3,
#    "Paper cup" : 2,
#    "Milk" : 1,
#    "Coke" : 4,
#    "Book" : 5
#}
#a = input("Enter name of the item:")
#print(items[a])

#магазин, с задачами
items = {"Coffee": 7, "Pen": 3, "Paper cup":2, "Milk": 1, "Coke":4, "Book": 5}
choice = -1
while choice != 4:
    choice = int(input("Select menu 1)check stock 2)warehousing 3)release 4) exit : "))
    if choice == 1:
        b = input("Enter item: ")
        if b in items:
            print(f"Stock {items[b]}")
        else:
            print("Item not found")

    elif choice == 2:
        for item in items.items():
            print(item[0], item[1])

    elif choice == 3:
        item_update = input("Enter item and quantity: ").split()
        item_name = item_update[0]
        item_quantity = item_update[1]
        items[item_name] = item_quantity


