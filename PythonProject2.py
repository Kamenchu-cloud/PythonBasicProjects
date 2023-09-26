def main():
    # Create a list and add five values
    my_list = [10, 20, 30, 40, 50]

    # Create a tuple and add five values
    my_tuple = (10, 20, 30, 40, 50)

    # Create a set and add five values
    my_set = {10, 20, 30, 40, 50}

    # Create a dictionary to store your details
    my_dict = {
        "Name": "Ian Kamenchu",
        "Age": "27",
        "Country": "Kenya",
    }

    # Print length of each data type
    print("Length of my_list:", len(my_list))
    print("Length of my_tuple:", len(my_tuple))
    print("Length of my_set:", len(my_set))
    print("Length of my_dict:", len(my_dict))

    # Calculate the sum of the numbers in my_list using a for loop
    # initialize result to 0 first
    result = 0
    for x in my_list:
        # use the addition assignment operator to add each number in the loop
        # this is the same as result = result + x
        # instead of writing this, you shorten it using the += (addition assignment operator)
        result += x

    # put the print function outside of the for loop. so that it prints only once after for loop is done.
    print("result:", result)

    # Calculate numbers 1-5 using a while loop
    # initialize sum of numbers, and the first number to be used
    sum_of_5 = 0
    num = 1
    # while loop - repeats the block of code in it until the number is no longer less than or equal to 5
    while num <= 5:
        # increment the sum
        sum_of_5 += num
        # increase num by 1 so that it goes to the next one
        num += 1

    # print the total sum outside the while loop
    print("sum of 5 is: ", sum_of_5)

    # Use a for loop with a range function to print numbers 1-5
    # range function takes three paramters. first is the start - which number to start from
    # second is the stop - where to stop, this number is not included
    # third is break - this is not necessary unless you want it to have a specific sequence
    for i in range(1, 6):
        print(i)


if __name__ == "__main__":
    main()
