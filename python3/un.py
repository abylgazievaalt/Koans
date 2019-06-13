class Cl():
	def coroutine(self):
	    result = yield
	    yield result

	generator = coroutine(self)

	try:
	    generator.send(1 + 2)
	except TypeError as ex:
	   print(ex.args[0])
