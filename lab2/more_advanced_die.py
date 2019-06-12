"""
File:  more_advanced_die.py
Description: Implements a MoreAdvancedDie class that allows for setting the current roll. 
Inherits from the parent class AdvancedDie in module advanced_die
"""

from advanced_die import AdvancedDie

class MoreAdvancedDie(AdvancedDie):
	"""MoreAdvancedDie class that extends AdvancedDie and allows users to set the current roll"""
	
	def __init__(self, sides=6):
		"""Constructor for any-sided Die that takes the number of sides as a parameter; 
		if no parameter is given then default is 6-sided.
		Precondition: sides is an integer >=1.
		Postcondition: current roll of die between 1 and number of sides"""
		AdvancedDie.__init__(self,sides)

	def setRoll(self, roll):
		"""Sets current roll of die to specified value
		Precondition: must specify a roll parameter between 1 and number of sides
		Postcondition: current roll set to specified value
		Raises: TypeError if roll is not an integer
				Value error if roll < 1 or if roll > numSides"""

		# check preconditions
		if not isinstance(roll,int):
			raise TypeError("Roll must be an integer!")
		if roll > self._numSides:
			raise ValueError("Roll must be less than or equal to the number of sides!")
		if roll < 1:
			raise ValueError("Roll must be greater than or equal to 1!")

		# sets currentRoll to roll
		self._currentRoll = roll



