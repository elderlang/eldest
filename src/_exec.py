import eons
import logging
from .e___ import e___
from .Exceptions import *

class _exec (e___):
	def __init__(this):
		super().__init__(name="exec")
		this.arg.kw.required.append('execution')
		this.arg.mapping.append('execution')

	def Function(this):
		if (type(this.execution) != list):
			this.execution = [this.execution]

		currentContext = None
		try:
			currentContext = context # From globals
		except:
			pass

		this.executor.SetGlobal('context', this)

		failMessage = None
		try:
			for instruction in this.execution:
				exec(instruction, globals())
		except HaltExecution:
			return
		except Exception as e:
			failMessage = f"Error in execution of {this.execution}: {e}"
			logging.error(failMessage)

		this.executor.SetGlobal('context', currentContext)

		if (failMessage is not None):
			raise RuntimeError(failMessage)

		# NOTE: my return value should be set by _return.