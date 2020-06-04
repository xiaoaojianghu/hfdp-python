

###############################################################################
# Quack behaviors
###############################################################################
from abc import ABCMeta, abstractmethod


class QuackBehavior:
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class FakeQuack(QuackBehavior):
    def quack(self):
        print("Qwak")


###############################################################################
# Fly behaviors
###############################################################################

class FlyBehavior():
    __metaclass__ = ABCMeta

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")
