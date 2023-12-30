import eons

class Type (eons.Functor):
	def __init__(this, name="Type"):
		super().__init__(name)

		this.arg.kw.required.append('name')
		this.arg.kw.required.append('kind')

		this.arg.kw.optional['parameter'] = None
		this.arg.kw.optional['execution'] = []

	def Function(this):
		if (type(this.kind) != list):
			this.kind = [this.kind]

		parameters = None #TODO: reverse engineer inspect.parameters
		source = f"for instruction in {this.execution}: _exec(instruction)"
		eons.kind(this.kind)(
			None,
			this.name,
			parameters,
			source
		)

		
		