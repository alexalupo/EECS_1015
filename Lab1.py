print("\n---- Task 1: Three year investment return ----")

name = input("Name: ")
initial_amt = float(input("Initial amount: $"))
return_rate = input("Rate of return: %")
decimal = round(float(return_rate) / 100, 2)
print("Client: " + name.strip().title() + ", yearly rate of return multiplier: " + str(decimal))
end_one = initial_amt + initial_amt * decimal
end_two = end_one + end_one * decimal
end_three = end_two + end_two * decimal
print("Year 1 \tStarting Amount: $" + str(format(initial_amt, ".2f")) + "\t\tEnding Amount: $" + str(
    format(end_one, ".2f")) + "\nYear 2 \tStarting Amount: $" + str(
    format(end_one, ".2f")) + "\t\tEnding Amount: $" + str(
    format(end_two, ".2f")) + "\nYear 3 \tStarting Amount: $" + str(
    format(end_two, ".2f")) + "\t\tEnding Amount: $" + str(format(end_three, ".2f")))



print("\n----Task 2 Leetspeak converter ----")
user_str = input("Type a long string: ")
user_upper = user_str.upper()
# go through letters and replace if condition is True
user_upper = user_upper.replace("T", "7")
user_upper = user_upper.replace("A", "^")
user_upper = user_upper.replace("E", "3")
user_upper = user_upper.replace("I", "!")
user_upper = user_upper.replace("B", "8")
user_upper = user_upper.replace("O", ".")
user_upper = user_upper.replace("C", "<")
user_upper = user_upper.replace("S", "$")
print(user_upper)


print("\n---- Task 3: Substring highlighter ----")
user_sentence = input("Type a sentence at the prompt below: ")
user_substring = input("Enter substring below to highlight: ")
print("Sentence has " + str(len(user_sentence)) + " characters, substring has " + str(
    len(user_substring)) + " characters.")
print("Substring highlighted:")
a = user_sentence.find(user_substring)
user_length = len(user_substring)
upper_sentence = user_sentence.upper()

singled_string = user_sentence[a:a + user_length]
new_sentence = user_sentence[0:a] + "*" + singled_string.upper() + "* " + user_sentence[a + user_length + 1:]
print(new_sentence)


print("\n---- Task 4: Exponent ----")
user_exponent = input("Input exponent in the form x^y: ")
seperator = user_exponent.find("^")
first_num = user_exponent[:seperator]
second_num = user_exponent[seperator + 1:]
exponent = int(first_num) ** int(second_num)
print("Extracted numbers: " + first_num + " " + second_num)
print(str(user_exponent) + " = " + str(exponent))

# pause program until enter is pressed
print("\n---- Lab 2 Done ----")
input("Press enter to exit.")
