import random

print("\n---- Task 1: Simple order ----")
print("""**Select menu item**
(1) Coke  [$1.00]
(2) Dosa  [$2.50]
(3) Pizza [$2.25]
(4) Taco  [$1.50]
(5) Tea   [$1.00]
""")
wrong_choice = 0
wrong_age = 0
discount = 0
cost = 0
total_discount = 0
total_cost = 0
user_choice = int(input("Selection: "))
if user_choice > 5 or user_choice < 1:
    print("Invalid Selection - Setting amount to $0")
    wrong_choice = "wc"
elif user_choice == 1:
    cost = 1
elif user_choice == 2:
    cost = 2.50
elif user_choice == 3:
    cost = 2.25
elif user_choice == 4:
    cost = 1.50
elif user_choice == 5:
    cost = 1

print("""**Discount**
(C) Child [under 18] (50% discount)
(A) Adult [18-64]
(S) Senior [65+] (25% discount)""")
user_age = input("Selection age: ")
if user_age.upper() not in ["C", "A", "S"]:
    print("\'" + user_age + "\' is an invalid selection! Extra charge for you!")
    wrong_age = "wa"
if wrong_choice == "wc":
    cost = 0
    total_cost = 0
    discount = 0
    total_discount = 0
elif wrong_age == "wa":
    total_discount = (float(cost) * 0.25) * -1
    total_cost = float(cost) - total_discount
else:
    if user_age.upper() == "C":
        discount = 0.5
        total_discount = float(cost) * float(discount)
        total_cost = float(cost) - float(total_discount)
    elif user_age.upper() == "A":
        discount = 0
        total_cost = float(cost)
        total_discount = 0
    elif user_age.upper() == "S":
        discount = 0.25
        total_discount = discount * float(cost)
        total_cost = float(cost) - float(total_discount)

print("Amount: $" + str(format(cost, ".2f")) + "\nDiscount: $" + str(
    format(total_discount, ".2f")) + "\n--------------------" + "\nTotal: $" + str(format(total_cost, ".2f")))


print("\n---- Task 2: Draw circle ----")
x = -10
y = -10
radius = int(input("Input size between 1-10: "))
while radius > 10 or radius < 1:
    radius = int(input("Input size between 1-10: "))
for x in range(-10, 11):
    print()
    for y in range(-10, 11):
        if x ** 2 + y ** 2 <= radius ** 2:
            print('*', end='')
        else:
            print('.', end='')


print("\n---- Task 3: Dice pair expected value ----")

try_again = "Y"
while try_again.upper() == "Y":
    times_roll = int(input("Roll dice how many times? "))
    tally = 0
    for i in range(times_roll):
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        print("[" + str(dice_one) + "]" + "\t[" + str(dice_two) + "] --- " + str(dice_one + dice_two) + "\tRoll " + str(
            i + 1))
        tally += dice_one + dice_two

    average = tally / times_roll
    print("Average dice pair value: " + str(format(average, ".2f")))
    try_again = input("Try again [Y/N]? ")
    if try_again.upper() == "Y":
        continue


print("\n---- Task 4: Compute PI ----")
real_pi = 3.14159265359
user_terms = int(input("Input the number of terms, M: "))
sum = 0
for n in range(0, user_terms + 1):
    term = ((-1) ** n) / (2 * n + 1)
    sum += term
    print("n=" + str(n) + "  .  .  .  adding fraction: " + str((-1) ** n) + "/" + str(2 * n + 1))
    print("Our  pi = " + str(format(sum * 4, ".11f")))
    print("Real pi = " + str(real_pi))

# pause program until enter is pressed
print("\n---- Lab 3 Done ----")
input("Press enter to exit.")
