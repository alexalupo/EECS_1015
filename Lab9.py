import random

def task1():
    again="Y"
    while again.upper()=="Y":
        long=input("Enter a long sentence: ")
        remove=input("Remove words containing: ")
        without=[]
        with1=[]
        long=long.split()
        for word in long:
            if remove in word:
                without.append(word)
            else:
                with1.append(word)
        print(f"With substring: '",end="")
        count = 1
        for x in without:
            #print(count)
            if count==len(without):
                print(f"{x}", end="")
            else:
                print(f"{x} ",end="")

            count+=1
        print("\'")
        print(f"Without substring: '",end="")
        count=1
        for x in with1:
            if count==len(with1):
                print(f"{x}", end="")
            else:
                print(f"{x} ",end="")

            count+=1
        print("\'")
        again=input("Try again? [Y/N] ")
        if again.upper()=="Y":
            continue

def task2():
    def randomlist(N):
        random_list=[]
        for i in range(N):
            temp=random.randint(0,9)
            random_list.append(temp)
        print(random_list)
        return random_list
    def reshape(a_list,num_rows,num_cols):
        new_list=[]

        for i in range(num_rows):
            temp_list=[]
            for j in range(num_cols):
                temp_list.append(a_list[j])
            a_list=a_list[num_cols:]

            new_list.append(temp_list)
            temp_list=[]
        print(new_list)
        return new_list

    again="Y"
    while again.upper()=="Y":
        list_elements=int(input("List length: "))
        a=randomlist(list_elements)
        rows=int(input("Rows: "))
        cols=int(input("Cols: "))
        while rows*cols!=list_elements:
            print(f"Error: {rows}*{cols} != {list_elements}")
            rows = int(input("Rows: "))
            cols = int(input("Cols: "))
        print("Reshaped List")
        reshape(a,rows,cols)
        again=input("Try again? [Y/N] ")
        if again.upper()=="Y":
            continue

def task3():
    iteration = 0
    def find_duplicates(a_dict):
        duplicate = {}
        for key, value in a_dict.items():
            if value not in duplicate:
                duplicate[value] = [key]
            else:
                duplicate[value].append(key)
        new_dict={}
        for key,value in duplicate.items():
            if len(value)>1:
                new_dict[key]=value
                #print(key,value)

        return new_dict

    again="Y"
    while again.upper()=="Y":
        word_list=[]
        my_dict={}
        print("Input words, press enter to end.")
        counter=1
        first_input=input(f"[Input {counter:2}] Word: ")

        while first_input!="":
            counter+=1
            word_list.append(first_input)
            first_input = input(f"[Input {counter:2}] Word: ")

        nums=1
        for x in word_list:
            my_dict[nums]=x
            nums+=1
        print("Dictionary")
        print(my_dict)
        print("Duplicates")
        print(find_duplicates(my_dict))
        again=input("Try again? ")
        if again.upper()=="Y":
            continue

def task4():
    class rangeChecker():
        range_counter=1
        def __init__(self,name,min,max):
            assert max>min, f"Max ({max}) must be greater than min ({min})"
            self.id = rangeChecker.range_counter
            rangeChecker.range_counter += 1
            self.name = name
            self.min = min
            self.max = max
        def within_range(self, number):
            if self.min<=number<=self.max:
                return True
            else:
                return False
        def outside_range(self,number):
            if number<self.min or number>self.max:
                return True
            else:
                return False
        def print1(self):
            print(f"rangeChecker [{self.id:2}]  '{self.name:10}' - {self.min:8.2f} <= num <= {self.max:8.2f}")
    again="Y"
    while again.upper()=="Y":

        first=input("Range 0 Name, Min, Max: ")
        new1=first.split(",")
        first_obj = rangeChecker(new1[0], float(new1[1]), float(new1[2]))


        second = input("Range 1 Name, Min, Max: ")
        new2 = second.split(",")
        second_obj = rangeChecker(new2[0], float(new2[1]), float(new2[2]))

        
        third = input("Range 2 Name, Min, Max: ")
        new3 = third.split(",")
        third_obj = rangeChecker(new3[0], float(new3[1]), float(new3[2]))

        user_in_nums=input("Input list of numbers x1,x2,..,xn: ")
        user_list_of_nums=user_in_nums.split(",")


        x = rangeChecker.print1(first_obj)
        for i in range(len(user_list_of_nums)):
            user_list_of_nums[i] = float(user_list_of_nums[i])
            print(f"Inside range [{user_list_of_nums[i]:8.2f}]: ",end="")
            print(first_obj.within_range(user_list_of_nums[i]))

        
        y = rangeChecker.print1(second_obj)
        for i in range(len(user_list_of_nums)):
            user_list_of_nums[i] = float(user_list_of_nums[i])
            print(f"Inside range [{user_list_of_nums[i]:8.2f}]: ",end="")
            print(second_obj.within_range(user_list_of_nums[i]))

        
        z = rangeChecker.print1(third_obj)
        for i in range(len(user_list_of_nums)):
            user_list_of_nums[i] = float(user_list_of_nums[i])
            print(f"Inside range [{user_list_of_nums[i]:8.2f}]: ",end="")
            print(third_obj.within_range(user_list_of_nums[i]))


        
        x = rangeChecker.print1(first_obj)
        for i in range(len(user_list_of_nums)):
            user_list_of_nums[i] = float(user_list_of_nums[i])
            print(f"Outside range [{user_list_of_nums[i]:8.2f}]: ",end="")
            print(first_obj.outside_range(user_list_of_nums[i]))

        
        y = rangeChecker.print1(second_obj)
        for i in range(len(user_list_of_nums)):
            user_list_of_nums[i] = float(user_list_of_nums[i])
            print(f"Outside range [{user_list_of_nums[i]:8.2f}]: ",end="")
            print(second_obj.outside_range(user_list_of_nums[i]))

        
        z = rangeChecker.print1(third_obj)
        for i in range(len(user_list_of_nums)):
            user_list_of_nums[i] = float(user_list_of_nums[i])
            print(f"Outside range [{user_list_of_nums[i]:8.2f}]: ",end="")
            print(third_obj.outside_range(user_list_of_nums[i]))

        again=input("Try again? ")
        if again.upper()=="Y":
            continue










#done
print("--- Task 1 ---")
task1()

#done
print("\n--- Task 2 ---")
task2()

#done
print("\n--- Task 3 ---")
task3()

#done see if can make code less convoluted
print("\n--- Task 4 ---")
task4()
