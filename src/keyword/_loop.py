import eons
from .._keyword import _keyword
from .._eval import _eval
from .._exec import _exec

class _loop (_keyword):
	def __init__(this, name = eons.INVALID_NAME()):
		super().__init__(name)
	
	def BeforeFunction(this):
		this._break = False
