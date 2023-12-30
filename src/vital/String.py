import eons
from .._eval import _eval
from .._exec import _exec

class String (eons.Functor):
	def __init__(this, name="String"):
		super().__init__(name)

		this.feature.argMap = False

	def Function(this):
		template = this.args[0]
		arguments = this.args[1:]
		return template.format(*[_eval(arg) for arg in arguments])