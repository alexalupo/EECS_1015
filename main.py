##################################
# EECS1015 - York University
# Author: Michael S. Brown
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 8 starter code
#
##################################
import random


def print_student_info():
    print("Name: Alexa Lupo")
    print("Student ID: 219411305")
    print("Section B")
    print("Email: alupo@my.yorku.ca")


# class for task 2
class virus:
    pass


# class for task 1
class lotto_ticket:
    ticket_counter = 1

    def __init__(self):
        self.ticket_id = lotto_ticket.ticket_counter
        lotto_ticket.ticket_counter += 1
        my_set = set()
        while len(my_set) != 5:
            temp_lotto = random.randint(1, 20)
            my_set.add(temp_lotto)
        self.numbers = my_set
        print(my_set)

    # self.ticket_counter

    def print_ticket(self):
        user_set = self.numbers
        print(f"Ticket #[{lotto_ticket.ticket_counter}]", end="")
        for i in range(5):
            print(self.numbers)
        return self.numbers


def task0():
    print_student_info()


def lotto_draw():
    lotto_list = []
    while len(lotto_list) != 5:
        temp_comp = random.randint(1, 20)
        if temp_comp not in lotto_list:
            lotto_list.append(temp_comp)
    # print(lotto_list)
    return lotto_list


def task1():
    amount = 100
    print(f"You have ${amount}")
    amt_tickets = int(input("How many lotto tickets do you want [$2 each]? "))
    while amt_tickets * 2 > amount or amt_tickets < 0:
        print(f"You have ${amount}")
        amt_tickets = int(input("How many lotto tickets do you want [$2 each]? "))
    if amt_tickets == 0:
        # print final amt (unchanged)
        quit

    tickets = []

    for i in range(amt_tickets):
        # call class so prints different each iteration of the for loop
        tickets.append(lotto_ticket())
    """
    for x in tickets:
        print("hello"+str(x.ticket_counter))
    """
    # print(tickets)
    # print("this is a:...")
    # a = lotto_draw()
    print("--LOTTO DRAW--")
    for i in range(amt_tickets):
        temp=lotto_ticket()
        new=temp.print_ticket()
    for number in lotto_draw():
        print(f"{new} ", end="")
    print()
    enter = input("---Press enter to check your winnings---")
    # for each obj call print and return win
    # add win amt to total
    # if user amt >=2 repeat - while user_amt>=2 continue else break


def task2():
    pass


def main():
    task0()
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()


if __name__ == "__main__":
    main()
