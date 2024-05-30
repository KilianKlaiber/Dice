# Create a class called Dice. Create a method roll_die. Create an object die and roll the die 10 times.

class Dice:
    '''
    Class of objects called Dice. The number of sides of each die is 6 by default.
    Rolling a die returns a random number between 1 and 6 or the specified number of sides.
    '''
    def __init__(self, sides: int=6) -> None:
        '''
        Create a die. 
        sides (integer): The number of sides of the die.
        '''
        self.sides = sides
    
    def roll_die(self) -> int:
        '''
        Roll the die
        return: A random number between 1 and the number of sides of the die.
        '''
        try:
            int(self.sides)
        except:
            print("\nYou did not enter a positive integer for the number of sides.")
            self.sides = 6
            print(f"The number of sides of the die has been set to: 6")
        if self.sides < 1 or int(self.sides) < self.sides:
            print("\nYou did not enter a positive integer for the number of sides.")
            self.sides = 6
            print(f"The number of sides of the die has been set to: 6")
       
        from random import randint
        return randint(1,self.sides)

# Create a die with n sides
die = Dice(0)
roll = die.roll_die()
print(f"\nYou have rolled the die. The result is: {roll}")

# Input the number of sides of the die


""" flag = True
while flag:
    try:
        number_sides = input("Enter the number of sides of the die: ")
        number_sides = int(number_sides)
    except:
        print("You must enter a positive integer.\n")
        continue    
    if number_sides < 1:
        print("You must enter a positive integer.\n")
    else:
         flag = False """

# Alternative code for inputting the number of sides
""" flag = True
while flag:
    try:
        n = input("Enter the number of sides of the die: ")
        n = int(n)
    except:
        print("You must enter a positive integer.")
    else:
        if n < 1:
            print("You must enter a positive integer.\n")
        else:
            flag = False"""




""" flag = True
while flag:
    result = die.roll_die()
    print(f"You have rolled: \t{result}")
    again = input("Do you want to roll the die again? (Yes/No)")
    again = again.lower()
    if again == "no":
        flag = False """
