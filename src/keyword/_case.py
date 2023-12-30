from .._keyword import _keyword
from .._eval import _eval
from .._exec import _exec

class _case (_keyword):
	def __init__(this):
		super().__init__(name = "case")

		this.arg.kw.required.append('condition')
		this.arg.kw.required.append('execution')
		this.arg.kw.required.append('_switch')

	def Function(this):
		if (this.condition == this._switch.condition):
			this._switch.matched = this
			_exec(this.execution)