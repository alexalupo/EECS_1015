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

def task0():
    print_student_info()

class lotto_ticket:
  ticket_counter = 1

  def __init__(self):
    self.ticket_id = lotto_ticket.ticket_counter
    lotto_ticket.ticket_counter+=1
    self.numbers = lotto_draw()

  def print_ticket(self):
    print(f"Ticket #[{self.ticket_id:3}]",end="")
    for i in self.numbers:
        print(f"  {i:2} ",end="  ")
    print()

  def print_and_return_win(self,lotto_numbers):
    user_same = list(lotto_numbers.intersection(self.numbers))
    if len(user_same) in [0,1,2]:
      win=0
    elif len(user_same) == 3:
      win = 2
    elif len(user_same) == 4:
      win = 20
    elif len(user_same) == 5:
      win = 100
    print(f"Ticket #[{self.ticket_id:3}] ", end="")
    for i in list(self.numbers):
      if user_same.count(i) == 1:
        print(f" *{i:2}*", end=" ")
      else:
        print(f"  {i:2}", end="  ")
    print(f"[{len(user_same)} matches, ${win}]")
    return win

def lotto_draw():
  computer_set=set()
  while len(computer_set)!=5:
    temp_computer=random.randint(1,20)
    computer_set.add(temp_computer)
  #print(computer_set)
  return computer_set

def task1():
  amount = 100
  while amount > 0:
    while True:
      print(f"You have ${amount}.")
      user_ticket_amt = input("How many lotto tickets do you want [$2 each]? ")
      if user_ticket_amt.isnumeric():
        user_ticket_amt = int(user_ticket_amt)
        if user_ticket_amt*2>=0 or user_ticket_amt*2<=amount:
          amount-=(user_ticket_amt*2)
          break
    if user_ticket_amt == 0:
      break
    comp_tickets = []
    for i in range(user_ticket_amt):
      comp_tickets.append(i)
      comp_tickets[i] = lotto_ticket()
      lotto_ticket.print_ticket(comp_tickets[i])

    print("--LOTTO DRAW--")
    comp_values=lotto_draw()
    for value in comp_values:
      print(f"{value:2} ",end="")
    #print(comp_values)
    print()

    user_enter=input("---Press enter to check your winnings--- ")
    total_win = 0
    for i in range(user_ticket_amt):
      win = lotto_ticket.print_and_return_win(comp_tickets[i], comp_values)
      total_win += win
    amount += total_win
  print(f"You have ${amount}.")

class virus:
  def __init__(self, DNAinput=""):
    if len(DNAinput) != 50:
      for i in range(50):
        random_dna = random.choice(["A","G","T","C"])
        DNAinput+=random_dna
    self.DNA = DNAinput

  def getDNA(self):
    return self.DNA

  def replicate(self):
    random_num = random.randint(1,100)
    if random_num > 94:
      change_dna=random.randint(0, 49)
      mutation=self.DNA[change_dna]
      DNA_list=["A","C","G","T"]
      ch_1=""
      if mutation.upper()=="A":
        DNA_list.remove("A")
        ch_1 = DNA_list[random.randint(0,2)]
      elif mutation=="C":
        DNA_list.remove("C")
        ch_1 = DNA_list[random.randint(0,2)]
      elif mutation=="G":
        DNA_list.remove("G")
        ch_1 = DNA_list[random.randint(0,2)]
      elif mutation=="T":
        DNA_list.remove("T")
        ch_1 = DNA_list[random.randint(0,2)]
      DNASequence=self.DNA[:change_dna]+ch_1+self.DNA[change_dna+1:]
      vir1=virus(DNASequence)
    else:
      vir1=virus(self.DNA)
    return vir1


def find_mutation(virus1,virus2):
  diff = ""
  virus1=virus.getDNA(virus1)
  virus2=virus.getDNA(virus2)
  for i in range(50):
    if virus1[i]==virus2[i]:
      diff+=" "
    else:
      diff+="^"
  return diff

def task2():
  again="Y"
  while again.upper()=="Y":
    virus_name =input("Name of virus: ")
    comp_vir = virus()
    original_virus = comp_vir
    print(f"Original DNA sequence: {virus.getDNA(comp_vir)}")
    while True:
      user_repeat=input("How many times to replicate? ")
      if user_repeat.isnumeric():
        user_repeat = int(user_repeat)
        if user_repeat >= 0:
          break
    for i in range(user_repeat):
      comp_vir = virus.replicate(comp_vir)
      print(f"Replica [{i:4}] DNA sequence: {virus.getDNA(comp_vir)}")

    print(f"Comparing latest {virus_name} virus to the original {virus_name}.")
    print(virus.getDNA(original_virus))
    print(virus.getDNA(comp_vir))
    mutation_mark = find_mutation(original_virus, comp_vir)
    mutation_num = mutation_mark.count("^")
    if mutation_num == 0:
      print("No mutations detected.")
    elif mutation_num <= 5:
      print(mutation_mark)
      print(f"{mutation_num} mutations -- virus is the same.")
    else:
      print(mutation_mark)
      print(f"{mutation_num} mutations -- a *new* virus has been created.")
    again = input("Try again? ")
    if again.upper()=="Y":
      continue

def main():
    task0()
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()

if __name__ == "__main__":
    main()