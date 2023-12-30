import eons
import re
from .._eval import _eval
from .._exec import _exec

class Autofill (eons.Functor):
	def __init__(this, name="Autofill"):
		super().__init__(name)

		this.arg.kw.required.append('source')
		this.arg.kw.required.append('target')

		this.arg.mapping.append('source')
		this.arg.mapping.append('target')

	def Function(this):
		source = _eval(this.source)

		target = eons.util.DotDict()
		target.name = None
		target.type = 0

		if (not '(' in this.target):
			target.name = this.target
			target.type = 1
		elif (
			this.target.startswith('Within')
			or this.target.startswith('Invoke')
		):
			search = re.search(r'\(name = (.*?),', this.target)
			target.name = search.group(1)
			target.type = 2
		elif (
			this.target.startswith('Call')
			or this.target.startswith('Sequence')
			or this.target.startswith('Get')
		):
			search = re.search(r'\((.*?),', this.target)
			target.name = search.group(1)
			target.type = 3

		if (target.name == None or target.type == 0):
			raise RuntimeError(f"Invalid target for autofill on {source}: {this.target}")

		try:
			# If member access works, use that.
			source = getattr(source, target.name)
			if (target.type == 1):
				return source
			elif (target.type == 2):
				newTarget = this.target.replace(f"name = {target.name}", f"source = {source}")
				return _eval(newTarget)
			elif (target.type == 3):
				newTarget = this.target.replace(f"{target.name},", f"{source},")
				return _eval(newTarget)
		except:
			# Otherwise, treat the source as a function.
			return source(_eval(this.target))
