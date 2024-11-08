
print('\n---- Task 1: Currency converter ----'+"\n")

ca_dollar=float(input("Amount in Canadian dollars: "))

us_dollar=ca_dollar*0.76
euro=ca_dollar*0.75
ng_naira=ca_dollar*322.24
cn_renminbi=ca_dollar*5.25
in_rupee=ca_dollar*97.14

print("Amount in other currencies: ")
print("USD: "+str(us_dollar)+"\n"+"EUR: "+str(euro)+"\n"+"NGN: "+str(ng_naira)+"\n"+"CNY: "+str(cn_renminbi)+"\n"+"INR: "+str(in_rupee))


print('\n---- Task 2: String math ----')


print("\n"+"Enter three strings: ")

str_1=input("str1: ")
str_2=input("str2: ")
str_3=input("str3: ")
print("\n"+"String concatenation: ")

print("str1 + str2 + str3 = "+str(str_1+str_2+str_3))
print("str3 + str2 + str1 = "+str(str_3+str_2+str_1))
print("str2 + str1 + str3 = "+str(str_2+str_1+str_3)+"\n")

user_int=int(input("Input an integer: "))

print("\n"+"String multiply: ")
print("num x str1 = "+str_1*user_int)
print("num x str2+str3 = "+(str_2+str_3)*user_int)


print("\n---- Task 3: Math operators ----"+"\n")
#gets user integer input
int_x=int(input("Input integer x: "))
int_y=int(input("Input integer y: "))

print("\n"+"Integer math:")

print("x / y = "+str(int_x/int_y))

print("x // y = "+str(int_x//int_y))

print("x % y = "+str(int_x%int_y))

print("x ** y = "+str(int_x**int_y)+"\n")

float_x=float(input("Input float x: "))
float_y=float(input("Input float y: "))
print("\n"+"Float math: ")

print("x / y = "+str(float_x/float_y))

print("x // y = "+str(float_x//float_y))

print("x % y = "+str(float_x%float_y))

print("x ** y = "+str(float_x**float_y)+"\n")



print('\n---- Task 4: Simple cylinder computation ----'+"\n")

pi=355/113

radius=float(input("Radius: "))
height=float(input("Height: "))

surface_area=2*pi*radius*height+2*pi*(radius**2)
volume=pi*(radius**2)*height

print("Cylinder surface area: "+str(surface_area))
print("Cylinder volume: "+str(volume))


print("\n---- FINISHED ----")
input("Press enter to end.")
