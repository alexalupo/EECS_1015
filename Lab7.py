import random

class virus:
    pass


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


    def print_ticket(self):
        user_set = self.numbers
        print(f"Ticket #[{lotto_ticket.ticket_counter}]", end="")
        for i in range(5):
            print(self.numbers)
        return self.numbers


def lotto_draw():
    lotto_list = []
    while len(lotto_list) != 5:
        temp_comp = random.randint(1, 20)
        if temp_comp not in lotto_list:
            lotto_list.append(temp_comp)

    return lotto_list


def task1():
    amount = 100
    print(f"You have ${amount}")
    amt_tickets = int(input("How many lotto tickets do you want [$2 each]? "))
    while amt_tickets * 2 > amount or amt_tickets < 0:
        print(f"You have ${amount}")
        amt_tickets = int(input("How many lotto tickets do you want [$2 each]? "))
    if amt_tickets == 0:
        quit

    tickets = []

    for i in range(amt_tickets):
        # call class so prints different each iteration of the for loop
        tickets.append(lotto_ticket())
    """
    for x in tickets:
        print("hello"+str(x.ticket_counter))
    """

    print("--LOTTO DRAW--")
    for i in range(amt_tickets):
        temp=lotto_ticket()
        new=temp.print_ticket()
    for number in lotto_draw():
        print(f"{new} ", end="")
    print()
    enter = input("---Press enter to check your winnings---")


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
