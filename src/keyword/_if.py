from .._keyword import _keyword
from .._eval import _eval
from .._exec import _exec

class _if (_keyword):
	def __init__(this):
		super().__init__(name = "if")

		this.arg.kw.required.append('condition')
		this.arg.kw.required.append('execution')

	def Function(this):
		this.didExecute = False
		if (this.condition):
			this.didExecute = True
			_exec(this.execution)