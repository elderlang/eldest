from .._keyword import _keyword
from .._eval import _eval
from .._exec import _exec

class _continue (_keyword):
	def __init__(this):
		super().__init__(name = "continue")

	def Function(this):
		loop = None
		for name, object in this.executor.stack.reverse():
			if (isinstance(object, _loop)):
				loop = object
				break

		if (loop is None):
			raise RuntimeError("Cannot continue outside of loop")

		loop.context.Halt()