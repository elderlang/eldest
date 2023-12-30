from .._type import _type

class _int(_type):
	def __init__(this, name="integer", value=0):
		super().__init__(name)

		this.value = value