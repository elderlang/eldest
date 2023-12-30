import eons

class EldestFunctor (eons.Functor):
	def __init__(this, name=eons.INVALID_NAME()):
		super().__init__(name)

		this.arg.kw.optional['context'] = None

		this.fetch.use = [
			'this',
			'args',
			'stack',
			'globals',
			# 'config', #local (if applicable) or per Executor; should be before 'executor' if using a local config.
			# 'precursor',
			# 'caller',
			# 'executor',
			# 'environment',
		]

	def BeforeFunction(this):
		this.executor.stack.append(
			(this.name, this)
		)

		if (this.context is None):
			this.context = this.executor.context

	def AfterFunction(this):
		this.executor.stack.remove(
			(this.name, this)
		)

	def fetch_location_stack(this, varName, default, fetchFrom, attempted):
		for name, object in this.executor.stack.reverse():
			if (name == varName):
				return object, True
		return default, False