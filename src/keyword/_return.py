from .._keyword import _keyword
from .._eval import _eval
from .._exec import _exec

class _return (_keyword):
	def __init__(this):
		super().__init__(name = "return")

		this.arg.kw.required.append('parameter')

	def Function(this):
		this.context.result.data.returned = _eval(this.parameter)
		this.context.Halt()