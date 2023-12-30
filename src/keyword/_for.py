from ._loop import _loop
from .._eval import _eval
from .._exec import _exec

class _for (_loop):
	def __init__(this):
		super().__init__(name = "for")

		this.arg.kw.required.append('source')
		this.arg.kw.required.append('container')
		this.arg.kw.required.append('execution')

	def Function(this):
		exec(f"""\
for {this.container[1:-1]} in this.source:
	_exec(this.execution)
	if (this._break):
		break
""")
