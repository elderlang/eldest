from .._type import _type

class _string(_type):
	def __init__(this, name="string", value=""):
		super().__init__(name)

		this.value = value