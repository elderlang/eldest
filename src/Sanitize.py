import eons
import re

class Sanitize (eons.Functor):

	keywords = [
		'break',
		'continue',
		'case',
		'default',
		'else',
		'for',
		'if',
		'not',
		'return',
		'switch',
		'while',
	]

	types = [
		'bool',
		'float',
		'int',
		'string',
		'null',
		'functor',
	]

	symbols = {
		'!': 'not',
		'=': 'eq',
		'&': 'and',
		'|': 'or',
		'>': 'gt',
		'<': 'lt',
		'+': 'plus',
		'-': 'minus',
		'*': 'times',
		'/': 'divide',
		'^': 'pow',
		'%': 'mod',
	}

	def __init__(this, name="Sanitize"):
		super().__init__(name)

		this.arg.kw.required.append('input')

		
	def Function(this, input):
		for keyword in this.keywords:
			input = re.sub(rf'\b{keyword}\b', rf'_{keyword}', input)
		for type in this.types:
			input = re.sub(rf'\b{type}\b', rf'_{type}', input)
		for symbol,replacement in this.symbols.items():
			input = re.sub(rf'\b{symbol}\b', rf'_{replacement}', input)
		return input