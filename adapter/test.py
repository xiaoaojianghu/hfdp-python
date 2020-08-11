from adapter.ducks import MallardDuck, TurkeyAdapter
from adapter.turkey import DuckAdapter, WildTurkey


def turkey_test_drive():
	# Turkey Test Drive
	duck = MallardDuck()
	duckAdapter = DuckAdapter(duck)

	for i in range(10):
		print "The DuckAdapter says..."
		duckAdapter.gobble()
		duckAdapter.fly()


def duck_test_drive():
	def test_duck(duck):
		duck.quack()
		duck.fly()

	# Duck Test Drive
	duck = MallardDuck()
	turkey = WildTurkey()
	turkeyAdapter = TurkeyAdapter(turkey)

	print "The Turkey says..."
	turkey.gobble()
	turkey.fly()

	print "\nThe Duck says..."
	test_duck(duck)

	print "\nThe TurkeyAdapter says..."
	test_duck(turkeyAdapter)


if __name__ == '__main__':
	turkey_test_drive()
	duck_test_drive()
