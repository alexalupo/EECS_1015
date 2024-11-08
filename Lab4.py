num_of_jumps = 0

my_list = []

import time
from random import randint


def get_int_input(prompt, min_value, max_value):
    user_num = int(input(prompt))
    while user_num < min_value or user_num > max_value:
        user_num = int(input(prompt))
    return user_num


def get_float_input(prompt, min_value, max_value):
    user_amount = float(input(prompt))
    while user_amount < min_value or user_amount > max_value:
        user_amount = float(input(prompt))
    my_list.append(user_amount)
    return user_amount


def get_yes(prompt):
    user_bool = input(prompt)
    while user_bool.upper() not in ["Y", "N"]:
        user_bool = input(prompt)
    if user_bool.upper() == "Y":
        return True
    elif user_bool.upper() == "N":
        return False


def draw_owl(position, randomize):
    eye1 = '{o,o}'
    eye2 = '{-,o}'
    eye3 = '{o,-}'
    body = '/)_) '
    feet = ' " " '
    if randomize == False:
        print((" " * position) + eye1 + "\n" + (" " * position) + body + "\n" + (" " * position) + feet)
    else:
        eyes = randint(1, 3)
        if eyes == 1:
            eyes = eye1
        elif eyes == 2:
            eyes = eye2
        else:
            eyes = eye3
        print((" " * position) + eyes + "\n" + (" " * position) + body + "\n" + (" " * position) + feet)


def compute_return(amount, rate, years):
    for i in range(years):
        new_amount = amount + amount * (rate)
        amount = new_amount
    if years == 1:
        print("Return in 1 year is: $" + format(new_amount, ".2f"))
    else:
        print("Return in " + str(years) + " years is: $" + format(new_amount, ".2f"))


def task1():
    a = get_int_input("How many times to move [2-20]? ", 2, 20)
    b = get_int_input("How long to delay [1-1000ms]? ", 1, 1000)
    c = get_yes("Randomize [Y/N]? ")
    for i in range(a):
        if c == True:
            draw_owl(i, True)
            time.sleep(b / 1000)
        else:
            draw_owl(i, False)
            time.sleep(b / 1000)


def task2():
    user_yes_or_no = "Y"
    while user_yes_or_no == "Y":
        my_list = []
        a = get_float_input("Input initial investment amount [1, 10000]? ", 1, 10000)
        b = get_float_input("Annual return rate [0-1]? ", 0, 1)
        c = get_int_input("How many years [1-10]? ", 1, 10)
        d = compute_return(a, b, c)
        e = get_yes("Compute new investment [Y/N]? ")
        if e == False:
            user_yes_or_no = "F"


def task3():
    global num_of_jumps
    for i in range(5):
        user_int = get_int_input(str(i + 1) + "/5\t  " + "Enter a number [1-100]: ", 1, 100)
        if num_of_jumps < user_int and user_int % 2 == 1:
            num_of_jumps = user_int
    if num_of_jumps % 2 == 0:
        num_of_jumps = 1
    print("Final max odd number: " + str(num_of_jumps) + ".")
    return num_of_jumps


def task4():
    frame1 = "  o   {step}\n /|\  \n / \  "
    frame2 = " \o/  {step}\n  |   \n / \  "
    if num_of_jumps == 1:
        start = input("Press enter to perform " + str(num_of_jumps) + " jumping jack.")
    else:
        start = input("Press enter to perform " + str(num_of_jumps) + " jumping jacks.")
    for i in range(num_of_jumps):
        if i % 2 == 0:
            print(frame2.format(step="[ " + str(i + 1) + "]"))
            time.sleep(0.3)
        else:
            print(frame1.format(step="[ " + str(i + 1) + "]"))
            time.sleep(0.3)


def main():
    print_student_info()
    print("\n---- Task 1: The Owl ----")
    task1()
    print("\n---- Task 2: Compound investment ---")
    task2()
    print("\n---- Task 3: Max odd number ----")
    task3()
    print("\n---- Task 4: Jumping Jacks ----")
    task4()
    input("Press enter to end lab 4.")


if __name__ == "__main__":
    main()
