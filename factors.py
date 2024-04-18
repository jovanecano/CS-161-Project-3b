# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 04/17/2024
"""Description: This program asks the user to enter a positive integer, then prints a list of all
 positive integers that divide that number evenly, including itself and 1, in ascending order"""

pos_integer = int(input("Please enter a positive integer: ")) # asking for user input
print(f"The factors of {pos_integer} are:")

for num in range(1, pos_integer+1): # for loop that loops through 1 to pos_integer (user input)
    if pos_integer % num == 0: # checks for factors of pos_integer
        print(f"{num}") # prints each factor of pos_integer