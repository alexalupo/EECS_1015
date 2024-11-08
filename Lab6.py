import random

def average_num(*nums):
    total = 0
    counter = 0
    for i in nums:
        total += i
        counter += 1
    formatted_average = format(total / counter, ".2f")
    print(f"Average is {formatted_average}")


def task1():
    again = "Y"
    while again.upper() == "Y":
        num_of_nums = int(input("Input 4 or 5 numbers? "))
        while num_of_nums not in [4, 5]:
            num_of_nums = int(input("Input 4 or 5 numbers? "))
        x1 = 0
        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        # 5 nums
        if num_of_nums == 5:
            five_nums = input("Input 5 numbers [x1, x2, x3, x4, x5] : ")
            five_split = five_nums.split(",")
            while len(five_split) != 5:
                five_nums = input("Input 5 numbers [x1, x2, x3, x4, x5] : ")
                five_split = five_nums.split(",")

            iteration = 0
            for i in five_split:
                if iteration == 0:
                    x1 = int(i)
                    iteration += 1
                elif iteration == 1:
                    x2 = int(i)
                    iteration += 1
                elif iteration == 2:
                    x3 = int(i)
                    iteration += 1
                elif iteration == 3:
                    x4 = int(i)
                    iteration += 1
                elif iteration == 4:
                    x5 = int(i)
                    iteration += 1
            average_num(x1, x2, x3, x4, x5)
        else:
            four_nums = input("Input 4 numbers [x1, x2, x3, x4] : ")
            four_split = four_nums.split(",")
            while len(four_split) != 4:
                four_nums = input("Input 4 numbers [x1, x2, x3, x4] : ")
                four_split = four_nums.split(",")

            iteration = 0
            for i in four_split:
                if iteration == 0:
                    x1 = int(i)
                    iteration += 1
                elif iteration == 1:
                    x2 = int(i)
                    iteration += 1
                elif iteration == 2:
                    x3 = int(i)
                    iteration += 1
                elif iteration == 3:
                    x4 = int(i)
                    iteration += 1
            average_num(x1, x2, x3, x4)

        again = input("Try again? ")
        if again.upper() == "Y":
            continue

def print_stock_dict(stock_dict):
    keys = list(stock_dict.keys())
    print("{:10s} {:6s}  {}".format("Symbol", "Price", "Company Name"))
    print("-" * 31)
    for k in keys:
        print(f"{k:7s} {stock_dict[k][1]:8.2f}   {stock_dict[k][0]}")
        # stock_dict[k][1]
        # ^^^^^^^^^^^^^    <- this gets the list for the key k
        #              ^^^ <- this retrieves item [1] in the list (price of stock)
        #
    print()  # <- an extra empty print to make it look nice


def string_to_stock_dict(*astring):
    string_stock_dict = {}
    split_user = asting.split(":")


def task2():
    stock_dict1 = {"SNAP": ["Snap", 10.08], "PINS": ["Pinterest", 29.40], "GOOG": ["Google", 96.58]}
    stock_list_string = "Apple:155.74:AAPL Tesla:228.52:TSLA Ford:13.26:F Microsoft:9.12:MSFT Shopify:34.19:SHOP"
    print_stock_dict(stock_dict1)
    # uncomment code for task4
    stock_dict2 = build_stock_dict(stock_list_string)
    print_stock_dict(stock_dict2)

def create_rand_list():
    random_list = []
    num_of_element = random.randint(5, 15)
    min_value = random.randint(5, 10)
    max_value = random.randint(20, 50)
    for i in range(num_of_element):
        new_list_val = random.randint(min_value, max_value)
        random_list.append(new_list_val)

    return random_list


def print_list(a_list):
    print("---list---")
    if len(a_list) == 0:
        print("(empty)")
    else:
        for x in a_list:
            print(f"({x})->", end="")
        print("(end)")


def delete_item_from_list(a_list, item):
    if item in a_list:
        index_of_del = a_list.index(item)
        a_list.remove(item)
        return index_of_del
        print(a_list)
    else:
        return -1


def task3():
    y_or_n = "Y"
    a = create_rand_list()
    while y_or_n.upper() == "Y":
        print_list(a)
        delete = int(input("Item to delete: "))
        b = delete_item_from_list(a, delete)
        if b == -1:
            print(f"Item {delete} could not be deleted.")
        else:
            print(f"Item {delete} successfully deleted at position {b}.")
        y_or_n = input("Delete item [Y/N]? ")
        if y_or_n.upper() == "Y":
            continue


def print_image(text_image):
    """
    for i in text_image:
      print(i,end="")
      #print(text_image)
    """
    pass

"""
def uncompress_rle_image(rle_image):
    rle_list = []
    # print(rle_image[0][0][0])
    # print(rle_image[0])
    # rle_image has first values until len of list-1 but second value is only 0 bc each list las only one tuple value at 0th position

    # only works for first tuple in list
    # iterate through list of lists
    # for i in raneg len of list iterate through for loop
    for x in rle_image:
        # print(f"x value {x}")
        for i in x:
            # print(f"i value: {i}")
            # print(len(x))
            if len(x) > 1:
                print((i[0] * i[1]), end="")
            else:
                print(i[0] * i[1])


        # printing extra line after len 1 item when not wanted for output
        print()

        # print(x)
        # print(rle_image[0][i])
        # calculated_line=x[0]*x[1]
        # rle_list.append(calculated_line)
    print(rle_list)
"""
def uncompress_rle_image(rle_image):
    rle_list = []
    for x in rle_image:
        # print(f"x value {x}")
        for i in x:
            add_list_val=[]
            # print(f"i value: {i}")
            # print(len(x))
            #remove if statement - redundant - check
            #if len>1, add to list until iterated through all i values then add list to rle_list
            #else, add individual val to rle list
            print(x)
            if len(x) > 1:
                temp_lst=[]
                for k in range(len(x)):
                    collect_val=i[0]*i[1]
                    temp_lst.append(collect_val)
                print(f"the temp list: {temp_lst}")

            else:
                rle_list.append(i[0] * i[1])
        rle_list.append(add_list_val)
    print(rle_list)

    pass


def task4():
    rle_image1 = [[(5, '-')], [(2, ' '), (1, '|')], [(2, ' '), (1, '|')], [(1, ' '), (3, '-')]]
    rle_image2 = [[(9, ' '), (1, '.'), (1, '8'), (1, '.'), (1, ' ')], [(9, ' '), (3, '8'), (1, ' ')],
                  [(9, ' '), (3, '8'), (1, 'l')],
                  [(8, ' '), (1, 'j'), (4, '8'), (1, '.')], [(7, ' '), (1, '.'), (6, '8'), (1, '.')],
                  [(6, ' '), (1, '.'), (8, '8'), (1, '.')],
                  [(4, ' '), (1, '.'), (1, 'd'), (10, '8'), (1, 'b'), (1, '.'), (1, ' ')],
                  [(2, ' '), (1, '.'), (1, 'd'), (14, '8'), (1, 'b'), (1, '.')],
                  [(1, ' '), (1, '.'), (18, '8'), (1, 'b'), (1, '.')],
                  [(1, '.'), (21, '8')], [(22, '8')], [(3, '8'), (1, 'P'), (2, '"'), (1, '4'), (3, '8')],
                  [(1, '`'), (1, 'P'), (1, "'"), (5, ' '), (1, '.'), (4, ' '), (1, '.'), (5, ' '), (1, '`'), (1, 'q'),
                   (1, "'")],
                  [(1, ' '), (1, '`'), (1, '-'), (2, '.'), (4, '_'), (1, ':'), (2, ' '), (1, ':'), (4, '_'), (2, '.'),
                   (1, '-'),
                   (1, "'"), (1, ' ')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(9, ' '), (1, ':'), (2, ' '), (1, ':')], [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(9, ' '), (1, ':'), (2, ' '), (1, ':')],
                  [(7, ' '), (1, '\\'), (1, '('), (1, '/'), (1, '\\'), (1, ')'), (1, '\\'), (1, '/'), (1, ' '),
                   (1, 'm'), (1, 'h')]]
    rle_image3 = [[(52, '.')], [(52, '.')], [(25, '.'), (1, '/'), (1, '\\'), (25, '.')],
                  [(18, '.'), (6, '_'), (1, '/'), (2, '_'), (1, '\\'), (7, '_'), (17, '.')],
                  [(18, '.'), (2, '|'), (13, '-'), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (13, ' '), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (4, ' '), (1, '\\'), (3, '|'), (1, '/'), (4, ' '), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (3, ' '), (1, '['), (1, ' '), (1, '@'), (1, '-'), (1, '@'), (1, ' '), (1, ']'),
                   (3, ' '), (2, '|'), (17, '.')],
                  [(18, '.'), (2, '|'), (4, ' '), (1, '('), (1, ' '), (1, '.'), (1, ' '), (1, ')'), (4, ' '), (2, '|'),
                   (7, '.'), (7, ' '), (3, '.')],
                  [(18, '.'), (2, '|'), (4, ' '), (1, '_'), (1, '('), (1, 'O'), (1, ')'), (1, '_'), (4, ' '), (2, '|'),
                   (7, '.'), (1, '|'), (1, 'E'), (1, 'X'), (1, 'I'), (1, 'T'), (1, ' '), (1, '|'), (3, '.')],
                  [(18, '.'), (2, '|'), (3, ' '), (1, '/'), (1, ' '), (1, '>'), (1, '='), (1, '<'), (1, ' '), (1, '\\'),
                   (3, ' '), (2, '|'), (7, '.'), (1, '|'), (2, '='), (2, '>'), (1, ' '), (1, '|'), (3, '.')],
                  [(18, '.'), (2, '|'), (2, '_'), (1, '/'), (1, '_'), (1, '|'), (1, '_'), (1, ':'), (1, '_'), (1, '|'),
                   (1, '_'), (1, '\\'), (2, '_'), (2, '|'), (17, '.')], [(18, '.'), (17, '-'), (17, '.')], [(52, '.')],
                  [(52, '.')]]

    # uncomment code for task4
    print("\t\tImage 1\n")
    image1 = uncompress_rle_image(rle_image1)
    # print_image(image1)
    print_image(image1)
    print("\t\tImage 2\n")
    image2 = uncompress_rle_image(rle_image2)
    print_image(image2)
    print("\t\tImage 3\n")
    image3 = uncompress_rle_image(rle_image3)
    print_image(image3)


def main():
    task0()
    print("\n--- Task 1: Average numbers ---")

    task1()

    print("\n--- Task 2: Text to dictionary---")
    task2()
    print("\n--- Task 3: Deleting from list---")
    task3()

    print("\n--- Task 4: RLE decoding  ---")
    task4()

    input("Press enter to end lab 6.")


if __name__ == '__main__':
    main()
