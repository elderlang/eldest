import eons
from .EldestFunctor import EldestFunctor

class _keyword (EldestFunctor):
	def __init__(this, name=eons.INVALID_NAME()):
		super().__init__(name)
