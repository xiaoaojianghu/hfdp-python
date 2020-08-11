from abc import ABCMeta, abstractmethod


class Subject:
	__metaclass__ = ABCMeta

	@abstractmethod
	def registerObserver(self, observer):
		pass

	@abstractmethod
	def removeObserver(self, observer):
		pass

	@abstractmethod
	def notifyObservers(self):
		pass


class WeatherData(Subject):

	def __init__(self):
		self._observers = []  # core: keep observers list
		self._temperature = None
		self._humidity = None
		self._pressure = None

	def registerObserver(self, observer):
		self._observers.append(observer) # register: add to list

	def removeObserver(self, observer):
		try:
			self._observers.remove(observer)
		except:
			pass

	def notifyObservers(self):
		for obs in self._observers:
			obs.update(self._temperature, self._humidity, self._pressure)

	def measurementsChanged(self):
		self.notifyObservers()

	def setMeasurements(self, temperature, humidity, pressure):
		self._temperature = temperature
		self._humidity = humidity
		self._pressure = pressure

		self.measurementsChanged()
