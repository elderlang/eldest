from .._keyword import _keyword
from .._eval import _eval
from .._exec import _exec
from ._loop import _loop

class _break (_keyword):
	def __init__(this):
		super().__init__(name = "break")

	def Function(this):
		loop = None
		for name, object in this.executor.stack.reverse():
			if (isinstance(object, _loop)):
				loop = object
				break

		if (loop is None):
			raise RuntimeError("Cannot break outside of loop")

		loop._break = True
		loop.context.Halt()