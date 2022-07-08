from webbrowser import get


my_list = {}

def add_item():
    shopping = True
    print("\nTo stop adding type: 'quit'")
    while shopping:
        item = input('\nWhat would you like to add? ')
        item = item.lower().strip()
        if item != 'quit':
            number = input(f'\nHow many {item}s would you like to add: ')
            if number.lower() == 'quit':
                print(f"\nNo {item}s added")
                shopping = False
            else:
                number = int(number)
                if item not in my_list:
                    my_list[item] = number
                else:
                    my_list[item] += number
        else:
            shopping = False

def del_item():
    deleting = True
    print("To stop deleting type: 'quit'")
    while deleting:
        item = input('\nWhat would you like to remove? ')
        item = item.lower().strip()
        if item == 'quit':
            deleting = False
            print('\nItem(s) removed')
        else:
            if item not in my_list:
                print('\nMaybe try deleting somthing you actually have....moron')
            else:
                number = input(f'\nHow many {item}s would you like to remove: ')
                if number.lower() == 'quit':
                    print(f"\nNo {item}s removed")
                    deleting = False
                else:
                    number = int(number)
                    if number > my_list[item]:
                        print(f"\nYou only had {my_list[item]} {item}s in your cart,\nso we removed them all")
                        del my_list[item]
                    else:
                        my_list[item] -= number
                        print(f'\nYou now have {my_list[item]} {item}(s)')
                        if item == 0:
                            del my_list[item]

def show_list():
    print("Your Shopping list: ")
    for item, quant in my_list.items():
        print(f"{item.title()} [{quant}]")

def get_price():
    price = 0
    for item, quant in my_list.items():
        if item[0] == 'a' or item[0] == 'b':
            price += (2.75 * quant)
        elif item[0] == 'c' or item[0] == 'd':
            price += (4.67 * quant)
        elif item[0] == 'e' or item[0] == 'f':
            price += (8.92 * quant)
        elif item[0] == 'g' or item[0] == 'h':
            price += (10.34 * quant)
        elif item[0] == 'i' or item[0] == 'j':
            price += (11.97 * quant)
        elif item[0] == 'k' or item[0] == 'l':
            price += (1.40 * quant)
        elif item[0] == 'm' or item[0] == 'n':
            price += (8.90 * quant)  
        elif item[0] == 'o' or item[0] == 'p':
            price += (15.67 * quant)     
        elif item[0] == 'q' or item[0] == 'r':
            price += (20.67 * quant)     
        elif item[0] == 's' or item[0] == 't':
            price += (12.67 * quant)     
        elif item[0] == 'u' or item[0] == 'v':
            price += (18.92 * quant)     
        elif item[0] == 'w' or item[0] == 'x':
            price += (7.61 * quant) 
        elif item[0] == 'y' or item[0] == 'z':
            price += (3.80 * quant)              
    return price
        



def shop_list():
    shopping = True
    while shopping:
        do = input('\nWould you like to show/add/delete or checkout: ')
        if do == 'add':
            add_item()
        elif do == 'delete':
            del_item()
        elif do == 'show':
            show_list()
        elif do == 'checkout':
            print("That will be: $", get_price(), sep='')
            last_call = input('\nLast Call: Edit or Continue ')
            if last_call.lower() == 'continue':
                print("Thank you for Shopping with Us!")
                shopping = False


shop_list()