from abc import ABCMeta, abstractmethod


class Duck:
	__metaclass__ = ABCMeta

	@abstractmethod
	def quack(self):
		pass

	def fly(self):
		pass


class MallardDuck(Duck):
	def quack(self):
		print "Quack"

	def fly(self):
		print "I'm flying"


class TurkeyAdapter(Duck):

	def __init__(self, turkey):
		self._turkey = turkey

	def quack(self):
		self._turkey.gobble()

	def fly(self):
		for i in range(5):
			self._turkey.fly()
