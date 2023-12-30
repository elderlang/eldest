from ._loop import _loop
from .._eval import _eval
from .._exec import _exec

class _while (_loop):
	def __init__(this):
		super().__init__(name = "while")

		this.arg.kw.required.append('parameter')
		this.arg.kw.required.append('execution')

	def Function(this):
		while (_eval(this.parameter) and not this._break):
			_exec(this.execution)
