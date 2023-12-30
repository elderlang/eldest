from .._keyword import _keyword
from .._eval import _eval
from .._exec import _exec

class _else (_keyword):
	def __init__(this):
		super().__init__(name = "else")

		this.arg.kw.required.append('_if')
		this.arg.kw.required.append('execution')
		

	def Function(this):
		if (not this._if.didExecute):
			_exec(this.execution)