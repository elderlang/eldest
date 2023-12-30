import eons
from .._type import _type
from .._eval import _eval
from .._exec import _exec

class _functor(_type):
	def __init__(this, name=eons.INVALID_NAME()):
		super().__init__(name)
		
	def Function(this):
		return _exec(this.execution)