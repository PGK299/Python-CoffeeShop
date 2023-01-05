# restaurant menu system
# ประกาสตัวแปร
coffee_list = ['Espresso', 'Cappucino', 'Latte']
coffee_type_list = ['Hot', 'Cold']
coffee_name = ''
coffee_type_select = ''
coffee_price = 0


# start menu
print()
print('---Welcome to Ohm coffee---')
print()

# show menu by input 1 (ถ้า input != 1 จะวนรับค่าเรื่อยๆ จนกว่าจะเป็น 1)
print()
while True:
    show_menu = int(input('Atlease type 1 to show menu: '))
    if show_menu == 1:
        break
print()

# show coffee menu
print('*', coffee_list[0])
print('*', coffee_list[1])
print('*', coffee_list[2])
print()


# วนรับค่า menu ถ้า input != 1,2,3 จะวนรับเรื่อยๆจนกว่าจะหยุด
while True:
    select_menu = int(input('Select coffee: '))
    if select_menu == 1:
        break
    if select_menu == 2:
        break
    if select_menu == 3:
        break

if select_menu == 1:
    coffee_name = coffee_list[0]
elif select_menu == 2:
    coffee_name = coffee_list[1]
elif select_menu == 3:
    coffee_name = coffee_list[2]

print()
print('--Choose the type of coffee--')
print('*', coffee_type_list[0])
print('*', coffee_type_list[1])
print()

# เลือก type
while True:
    coffee_type_select = int(input('Select type: '))
    if coffee_type_select == 1:
        break
    if coffee_type_select == 2:
        break

if coffee_type_select == 1:
    coffee_type_select = coffee_type_list[0]
    coffee_price = 55
elif coffee_type_select == 2:
    coffee_type_select = coffee_type_list[1]
    coffee_price = 60

#checkout & changes
print()
print('---You chose', coffee_type_select,
      coffee_name, coffee_price, 'baht ---')
while True:
    money_receive = int(input('Input your money: '))
    print()
    if money_receive >= coffee_price:
        coffee_price_change = money_receive-coffee_price
        print()
        print('You receieved a change of %d baht' % coffee_price_change)
        print('---Thank you---')
        print()
        break
    else:
        print('!!You money is not enough!!')
