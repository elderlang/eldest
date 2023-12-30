from .._type import _type

class _null(_type):
	def __init__(this, name="string"):
		super().__init__(name)

		this.value = False