__all__ = [
	'LockGuard',
	'AutoFetcher',
]

from Manifest import threading, time

class LockGuard:
	def __init__(self, lock):
		self.__lock = lock
	def __enter__(self):
		self.__lock.acquire()
	def __exit__(self, excClass, excObj, tb):
		self.__lock.release()

class AutoFetcher:
	def __init__(self, interval, changeCallback=None):
		self.__thread = threading.Thread(target=self.__updateForever)
		self.__interval = max(0, float(interval))
		self.__thread.daemon = True
		self.__thread.start()
		self.__lock = threading.Lock()
		self.__changeCallback = changeCallback

	def _lockGuard(self):
		return LockGuard(self.__lock)

	def __updateForever(self):
		while True:
			time.sleep(self.__interval)
			self._update()

	def _update(self):
		raise NotImplementedError()

	def _callChangeCallback(self):
		if self.__changeCallback:
			try:
				self.__changeCallback(self)
			except Exception, e:
				print ('Error calling %s: %s'
					% (self.__changeCallback, e))
				self.__changeCallback = None

	def isAlive(self):
		return self.__thread.isAlive()


