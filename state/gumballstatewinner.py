"""
Gumball machine with winner state

Author: m1ge7
Date: 2014/03/30
"""

from state.states import *


class GumballMachine:

	def __init__(self, number_gumballs):
		self.__sold_out_state = SoldOutState(self)
		self.__no_quarter_state = NoQuarterState(self)
		self.__has_quarter_state = HasQuarterState(self)
		self.__sold_state = SoldState(self)
		self.__winner_state = WinnerState(self)

		self.__state = self.__sold_state
		self.__count = number_gumballs
		if number_gumballs > 0:
			self.__state = self.__no_quarter_state

	def insert_quarter(self):
		self.__state.insert_quarter()

	def eject_quarter(self):
		self.__state.eject_quarter()

	def turn_crank(self):
		self.__state.turn_crank()

	def set_state(self, state):
		self.__state = state

	def release_ball(self):
		print "A gumball comes rolling out the slot..."
		if self.__count != 0:
			self.__count -= 1

	def get_count(self):
		return self.__count

	def refill(self, count):
		self.__count = count
		self.__state = self.__no_quarter_state

	def get_state(self):
		return self.__state

	def get_sold_out_state(self):
		return self.__sold_out_state

	def get_no_quarter_state(self):
		return self.__no_quarter_state

	def get_has_quarter_state(self):
		return self.__has_quarter_state

	def get_sold_state(self):
		return self.__sold_state

	def get_winner_state(self):
		return self.__winner_state

	def __str__(self):
		result = ""
		result += "\nMighty Gumball, Inc."
		result += "\nJava-enabled Standing Gumball Model #2004"
		result += "\nInventory: " + str(self.__count) + " gumball"
		if self.__count != 1:
			result += "s"
		result += "\n"
		result += "Machine is " + str(self.__state) + "\n"
		return result


if __name__ == '__main__':
	gumballmachine = GumballMachine(10)

	print(gumballmachine)

	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()
	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()

	print(gumballmachine)

	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()
	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()

	print(gumballmachine)

	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()
	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()

	print(gumballmachine)

	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()
	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()

	print(gumballmachine)

	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()
	gumballmachine.insert_quarter()
	gumballmachine.turn_crank()

	print(gumballmachine)
