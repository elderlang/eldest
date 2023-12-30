from .._type import _type

class _float(_type):
	def __init__(this, name="float", value=0.0):
		super().__init__(name)

		this.value = value