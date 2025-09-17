#Pizza concession 
Menu = { "Marghretia Pizza":399,
"Cheese & Corn Pizza": 499,"Cheese & Tomato Pizza":499,
"Double Cheese & Marghretia Pizza": 539, "Fresh Veggies Pizza":539,
"Farmhouse Pizza": 599,"Preppy paneer pizza":599,"Veggies Paradise Pizza":699,
"Cheese Dominator Pizza":839,"Cheese Pizza":839}
print("--------------------------------- Menu -------------------------")
Cart = []
Total=0
for Key, Value in Menu.items():
    print(f"{Key:35} - Rs.{Value:.2f}")
print("----------------------------------------------------------------")
while True:
    Food = input("Select an item (q for quite): ").lower().strip()
    if Food=='q':
        break
    Matched_item = None
    for key in Menu.keys():
        if key.lower() == Food.lower():
           Matched_item= key
           break
    if Matched_item:
      Cart.append(Matched_item)
      print(f"✅{Matched_item} is added to cart!")
    else:
      print("❌Item Not Available please choose from the menu")
print("------------------------- Your Order ---------------------------")
for food in Cart:
    Total += Menu.get(food)
    print(food)
print("----------------------------------------------------------------")
print (f"Your Total is Rs.{Total:.2f}")

