def adding(menu_items, item):
    if item not in menu_items:
        menu_items.append(item)
    return menu_items
def removing(menu_items, item):
    if item in menu_items:
        menu_items.remove(item)
    else:
        print(f"{item} does not found in the menu.")
    return menu_items

def checking(menu_items, item):
        if item in menu_items:
            return f"{item} is available"
        else:
            return f"{item} is not available"

menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
menu = adding(menu, add_item)

remove_item = "Salad"
menu = removing(menu, remove_item)

check_item = "Pizza"
availability = checking(menu, check_item)
print(f"Updated menu: {menu}")
print(f"Availability: {availability}")
