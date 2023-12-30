from .._type import _type

class _bool(_type):
	def __init__(this, name="bool", value=False):
		super().__init__(name)

		this.value = value