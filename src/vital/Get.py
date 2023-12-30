import eons
from .._eval import _eval
from .._exec import _exec

class Get (eons.Functor):
	def __init__(this, name="Get"):
		super().__init__(name)

		this.arg.kw.optional['name'] = None
		this.arg.kw.optional['source'] = None

		this.arg.kw.required.append('target')

		this.arg.mapping.append('name')
		this.arg.mapping.append('target')

	def Function(this):
		if (this.source is not None):
			return getattr(this.source, this.target)
		elif (this.name is not None):
			return getattr(_eval(this.name), this.target)
		
		raise RuntimeError(f"Neither source nor name was provided to {this.name}")