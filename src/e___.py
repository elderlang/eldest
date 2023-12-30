import eons
from ._keyword import _keyword
from .Exceptions import *

class e___ (_keyword):
	def __init__(this, name = eons.INVALID_NAME()):
		super().__init__(name)

		this._halt = False

	def BeforeFunction(this):
		this._halt = False

	def Halt(this):
		this._halt = True
		raise HaltExecution()