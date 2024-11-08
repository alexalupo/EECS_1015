################################
# EECS1015, York University
# Lab 5 starting code
# Name:  Alexa Lupo
# Section:  B
# Student ID: 219411305
# Email:  alupo@my.yorku.ca
################################

import random


# Print info
def print_lab_info():
    print("---- Lab 5 ----")
    print("Name: Alexa Lupo")
    print("Section B")
    print("Student id: 21941305")
    print("Email: alupo@my.yorku.ca")


def task0():
    # Example of calling a function from taskX() functions.
    # you should write all functions "outside" your task1()-task4() functions.
    print_lab_info()

def input_list():
    my_list = []
    user_int = int(input("Input positive int:"))
    my_list.append(user_int)
    while user_int >= 0:
        user_int = int(input("Input positive int:"))
        my_list.append(user_int)
    del my_list[-1]
    return my_list
def compute_average(aList):
    sum = 0
    for i in aList:
        sum += i
    if not len(aList) == 0:
        average = sum / int(len(aList))
    else:
        average = 0
    print("List average " + format(average, ".2f"))
    if int(len(aList)) == 0:
        return 0
    else:
        return average

def get_yes(prompt):
    user_yes_or_no = input(prompt)
    while user_yes_or_no.upper() not in ["Y", "N"]:
        user_yes_or_no = input(prompt)
    if user_yes_or_no.upper() == "Y":
        return True
    elif user_yes_or_no.upper() == "N":
        return False
def task1():
    #done
    user_yes_or_no = "Y"
    while user_yes_or_no == "Y":
        #my_list = []
        a=input_list()
        compute_average(a)
        if get_yes("Do again [Y/N]? ") == False:
            user_yes_or_no = False


def task2():
    # done
    string_list = []
    user_string = input("Input a long string: ")
    upper_user = user_string.upper()

    for i in upper_user:
        string_list.append(i)
    list_to_set = set(string_list)
    my_dict = {}
    for element in list_to_set:
        my_dict[element] = 0
    for j in upper_user:
        my_dict[j] += 1
    for key in my_dict:
        print("\'" + key + "\'" + "\t|" + str("*" * my_dict[key]))


def task3():
    encoder = {'A': '$', 'B': 'F', 'C': 'C', 'D': '2', 'E': 'B', 'F': 'I', 'G': '=', 'H': '*', 'I': '"', 'J': ']',
               'K': '1',
               'L': '0', 'M': '@', 'N': '[', 'O': 'L', 'P': '%', 'Q': '&', 'R': '(', 'S': 'G', 'T': 'K', 'U': '5',
               'V': '!',
               'W': '^', 'X': '+', 'Y': '6', 'Z': '-', '1': 'H', '2': 'A', '3': 'J', '4': '7', '5': '4', '6': 'D',
               '7': 'E',
               '8': '9', '9': ')', '0': ';', ',': '3', '.': '/', ' ': '_'}
    decoder = {'$': 'A', 'F': 'B', 'C': 'C', '2': 'D', 'B': 'E', 'I': 'F', '=': 'G', '*': 'H', '"': 'I', ']': 'J',
               '1': 'K',
               '0': 'L', '@': 'M', '[': 'N', 'L': 'O', '%': 'P', '&': 'Q', '(': 'R', 'G': 'S', 'K': 'T', '5': 'U',
               '!': 'V',
               '^': 'W', '+': 'X', '6': 'Y', '-': 'Z', 'H': '1', 'A': '2', 'J': '3', '7': '4', '4': '5', 'D': '6',
               'E': '7',
               '9': '8', ')': '9', ';': '0', '3': ',', '/': '.', '_': ' '}
    again = "Y"
    while again.upper() == "Y":
        user_string = input("Input message : ").upper()
        e_or_d = input("Encode (E) or Decode (D)? ")
        while e_or_d.upper() not in ["E", "D"]:
            e_or_d = input("Encode (E) or Decode (D)? ")
        message = []
        if e_or_d.upper() == "E":
            for i in user_string:
                message.append(encoder[i])
            print("".join(message))
        elif e_or_d.upper() == "D":
            for i in user_string:
                message.append(decoder[i])
            print("".join(message))
        again = input("Encode/decode again [Y/N]? ")
        if again.upper() == "Y":
            continue


num_set = {}


def random_set():
    global num_set
    my_set = {}
    num_set = set(my_set)
    while len(num_set) < 5:
        a = random.randint(1, 20)
        num_set.add(a)
    return num_set

def print_set(aSet, prompt=""):
    print(f"{prompt}",end="")
    for number in aSet:
        print(f"{number} ",end="")


def task4():
    # use set not list
    # while len of set is less than 6 keep generating numbers randomly
    """
    def random_set_try1():
      numbers=[]
      for i in range (5):
        a=random.randint(1,20)
        while a in numbers:
          a=random.randint(1,20)
        else:
          numbers.append(a)
      number_set=numbers.set()
      return number_set
    """



    # fix so repeats when num>20 <1 and len<5
    # while loop infinite redo wrong statement
    # bottom works
    # account for wrong input
    wrong = 0
    user_lotto = input("Enter 5 numbers between 1-20: ")
    individual_numbers = user_lotto.split()
    for i in individual_numbers:
        if int(i) > 20 or int(i) < 1 or len(individual_numbers)!=5:
            wrong = "a"

    if wrong == "a":
        print("wrong")
    else:
        individual_numbers = user_lotto.split()
        random_set()
        #prints random set
        print_set(num_set, "Computer set: ")
        print()
        #prints user set
        print_set(individual_numbers, "My set: ")
    same_list=[]
    for x in num_set:
        for y in individual_numbers:
            if int(x)==int(y):
                #print("\n same \n")
                same_list.append(x)
    matches=len(same_list)
    if matches!=1:
        es="es"
    else:
        es=""
    print()
    print(f"{matches} match{es} found: ",end="")
    for i in same_list:
        print(f"{i} ",end="")


def main():
    ### Don't forget to update print_lab_info() function
    # task0()

    print("\n---- Task 1: List average ----")
    # task1()

    print("\n---- Task 2: Character count graph ----")
    # task2()
    # fix so prints same output as lab sheet
    # clean .upper()

    print("\n---- Task 3: Encoder/decoder ----")
    # task3()

    print("\n---- Task 4: Lotto LESS ----")
    task4()


if __name__ == "__main__":
    main()