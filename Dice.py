# Create a class called Dice. Create a method roll_die. Create an object die and roll the die 10 times.

from random import randint

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
       
        return randint(1,self.sides)
