from random import shuffle
from database import DATABASE

RED = '\033[31m'
GREEN = '\033[32m'
RESET_COLORS = '\033[m'

ORDER_LIST = DATABASE['order_list']
DONE = DATABASE['done']

def new_order():
    global ORDER_LIST
    global DONE
    ORDER_LIST.clear()
    DONE.clear()

    first_question_number = 1
    last_qustion_number = int(input("What's the last question number? "))
    ORDER_LIST.extend(list(range(first_question_number, last_qustion_number+1)))
    DONE.extend([False] * len(ORDER_LIST))
    shuffle(ORDER_LIST)
    update_database()


def show_order():
    global ORDER_LIST
    global DONE
    global GREEN, RED, RESET_COLORS

    for index, question in enumerate(ORDER_LIST):
        question_done = DONE[index]
        color = GREEN if question_done else RED
        print(f'{color}{question} -- done: {question_done}{RESET_COLORS}')


def manager():
    show_order()
    done_question = int(input('What question you want to add as done? '))
    done_question_index = ORDER_LIST.index(done_question)
    DONE[done_question_index] = True
    update_database()


def update_database():
    global DATABASE

    database_write = open('database.py', 'w')
    database_write.write(f'DATABASE = {DATABASE}\n\n')
    database_write.close()


if __name__ == '__main__':
    print('type "set" to set another order')
    print('type "show" to show last order')
    print('type "manager" to manage your questions')
    print('type "help" to show this messages')
    print('type "exit" to exit')
    while True:
        answer = input('--> ')
        if answer == 'set':
            new_order()
        elif answer == 'show':
            show_order()
        elif answer == 'manager':
            manager()
        elif answer == 'exit':
            exit()

