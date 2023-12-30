import eons
from .._eval import _eval
from .._exec import _exec

class Sequence (eons.Functor):
	def __init__(this, name="Sequence"):
		super().__init__(name)

		this.arg.kw.optional['name'] = None
		this.arg.kw.optional['source'] = None

		this.arg.kw.required.append('target')

		this.arg.mapping.append('source')
		this.arg.mapping.append('target')

	def Function(this):
		if (this.source is not None):
			return this.source.__truediv__(_eval(this.target))
		elif (this.name is not None):
			return _eval(this.name).__truediv__(_eval(this.target))
		
		raise RuntimeError(f"Neither source nor name was provided to {this.name}")