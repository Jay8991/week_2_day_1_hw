#Exercise #1
#Create a calculator using functions that asks for two numbers and performs a calculation that the user inputs... 
# Loop until the user chooses not to perform any more calculations.

# getting two numbers from user
# getting which operator from user 
# getting if user wants to continue or no

def calculator():
    cont = "y"
    # loop until the user wants to
    while(cont == "y"):
        # get two numbers and operator from user
        num_one = int(input("choose number one: "))
        num_two = int(input("choose number two: "))
        operator = input("Choose which operator (+, -, /, *): ")
        # if elif statements depending which operator the user selected
        if operator == "+":
            print(num_one + num_two)
        elif operator == "-":
            print(num_one - num_two)
        elif operator == "*":
            print(num_one * num_two)
        elif operator == "/":
            print(num_one / num_two)
        else:
            print("Invalid operator")
        # ask user again if want to continue or not before looping again
        cont = input("Do you want to continue(y/n)? ").lower()

# check
calculator()



#Exercise 2
#Create a pyramid of X's for n number of levels.

def make_pyramid(n):
    for i in range(n):
        # print("Before loop began: ", end=' ')
        # print(i)
        number_of_x = (n-i)-1
        # spaces
        while(i != n-1):
            print("",end=" ")
            i = i + 1

        # print("After space loop: ", end=' ')
        # print(i)
        # prints correct number of x's
        while(number_of_x != n):
            print("X", end=' ')
            number_of_x = number_of_x + 1
        print("\n")
        
cont = "y"
while(cont == "y"):
    pyramid = int(input("How many number of levels do you want on your pyramid? "))
    make_pyramid(pyramid)
    cont = input("Do you want to continue(y/n)? ").lower()