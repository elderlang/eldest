from .._keyword import _keyword
from .._eval import _eval
from .._exec import _exec

class _not (_keyword):
	def __init__(this):
		super().__init__(name = "not")

		this.arg.kw.required.append('parameter')

	def Function(this):
		return not _eval(this.parameter)