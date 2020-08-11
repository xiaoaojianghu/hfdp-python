# -*- coding: utf-8 -*-

import random
from abc import ABCMeta, abstractmethod


class Turkey:
	__metaclass__ = ABCMeta

	@abstractmethod
	def gobble(self):
		pass

	@abstractmethod
	def fly(self):
		pass


class WildTurkey(Turkey):
	__metaclass__ = ABCMeta

	def gobble(self):
		print "Gobble gobble"

	def fly(self):
		print "I'm flying a short distance"


# 继承Turkey, 用duck init
class DuckAdapter(Turkey):

	# 用duck init
	def __init__(self, duck):
		self._duck = duck

	def gobble(self):
		self._duck.quack()

	def fly(self):
		if random.randint(0, 5) == 0:
			self._duck.fly()
