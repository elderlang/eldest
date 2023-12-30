from .._keyword import _keyword
from .._eval import _eval
from .._exec import _exec

class _default (_keyword):
	def __init__(this):
		super().__init__(name = "default")

		this.arg.kw.required.append('_switch')
		this.arg.kw.required.append('execution')

	def Function(this):
		if (this._switch.matched is None):
			this._switch.matched = this
			_exec(this.execution)