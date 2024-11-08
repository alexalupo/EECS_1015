########################################
# EECS1015- Fall 2022
# Lab 1
#
# Your name:
# Your section:
# Your student ID:
# Your email contact:
#######################################

# Please fill out your info for each lab
print("---- Lab 1 ----")
print("Name: Alexa Lupo")
print("Section B")
print("Student id: 219411305 ")
print("Email: alupo@my.yorku.ca")

# Task 1
print('\n---- Task 1: Currency converter ----'+"\n")
#user inputs amount they want to convert in CAD
ca_dollar=float(input("Amount in Canadian dollars: "))

#Converts CAD to different curriencies
us_dollar=ca_dollar*0.76
euro=ca_dollar*0.75
ng_naira=ca_dollar*322.24
cn_renminbi=ca_dollar*5.25
in_rupee=ca_dollar*97.14
#prints the conversions
print("Amount in other currencies: ")
print("USD: "+str(us_dollar)+"\n"+"EUR: "+str(euro)+"\n"+"NGN: "+str(ng_naira)+"\n"+"CNY: "+str(cn_renminbi)+"\n"+"INR: "+str(in_rupee))

# Task 2
print('\n---- Task 2: String math ----')

#user enters three strings
print("\n"+"Enter three strings: ")

str_1=input("str1: ")
str_2=input("str2: ")
str_3=input("str3: ")
print("\n"+"String concatenation: ")
#concatenates and prints the listed string additions
print("str1 + str2 + str3 = "+str(str_1+str_2+str_3))
print("str3 + str2 + str1 = "+str(str_3+str_2+str_1))
print("str2 + str1 + str3 = "+str(str_2+str_1+str_3)+"\n")
#collects user integer
user_int=int(input("Input an integer: "))
#prints string repetition based on user integer
print("\n"+"String multiply: ")
print("num x str1 = "+str_1*user_int)
print("num x str2+str3 = "+(str_2+str_3)*user_int)

# Task 3
print("\n---- Task 3: Math operators ----"+"\n")
#gets user integer input
int_x=int(input("Input integer x: "))
int_y=int(input("Input integer y: "))
#calculates and prints int math
print("\n"+"Integer math:")
#division
print("x / y = "+str(int_x/int_y))
#floor division
print("x // y = "+str(int_x//int_y))
#modulus
print("x % y = "+str(int_x%int_y))
#squared
print("x ** y = "+str(int_x**int_y)+"\n")
#gets user input for float
float_x=float(input("Input float x: "))
float_y=float(input("Input float y: "))
print("\n"+"Float math: ")
#calculates and prints float math
#division
print("x / y = "+str(float_x/float_y))
#floor division
print("x // y = "+str(float_x//float_y))
#modulus
print("x % y = "+str(float_x%float_y))
#squared
print("x ** y = "+str(float_x**float_y)+"\n")


# Task 4
print('\n---- Task 4: Simple cylinder computation ----'+"\n")
#initialized number pi
pi=355/113

#collect user input for radius and height
radius=float(input("Radius: "))
height=float(input("Height: "))
#uses user input to calculate surface area then volume
surface_area=2*pi*radius*height+2*pi*(radius**2)
volume=pi*(radius**2)*height
#prints sa and vol
print("Cylinder surface area: "+str(surface_area))
print("Cylinder volume: "+str(volume))

## Adding the final "input" causes python to wait on the user to press enter
## before exiting the program.
print("\n---- FINISHED ----")
input("Press enter to end.")