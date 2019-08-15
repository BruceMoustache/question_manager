from random import shuffle
from database import ORDER_LIST

def new_order():
    global ORDER_LIST
    first_question_number = 1
    last_qustion_number = int(input("What's the last question number? "))

    ORDER_LIST = list(range(first_question_number, last_qustion_number+1))
    shuffle(ORDER_LIST)
    database_write = open('database.py', 'w')
    database_write.write(f'ORDER_LIST = {ORDER_LIST}')


def show_order():
    global ORDER_LIST
    print(ORDER_LIST)


print('if you want to set another order type "set"')
print('if you want to show last order type "show"')
answer = input('--> ')
if answer == 'set':
    new_order()
elif answer == 'show':
    show_order()

