import eons
from .EldestFunctor import EldestFunctor

class _type(EldestFunctor):
	def __init__(this, name=eons.INVALID_NAME()):
		super().__init__(name)

		this.value = None

	def _eq(this, other):
		this = other
		return this

	def _gt(this, other):
		return this > other

	def _lt(this, other):
		return this < other

	def _eq_eq(this, other):
		return this == other
	
	def _not_eq(this, other):
		return this != other

	def _gt_eq(this, other):
		return this >= other

	def _lt_eq(this, other):
		return this <= other

	def _pow(this, other):
		return pow(this, other)

	def _and(this, other):
		return this and other

	def _and_and(this, other):
		return this._and(other)

	def _or(this, other):
		return this or other

	def _or_or(this, other):
		return this._or(other)

	def _plus(this, other):
		return this + other

	def _minus(this, other):
		return this - other

	def _times(this, other):
		return this * other

	def _divide(this, other):
		return this / other

	def _plus_eq(this, other):
		this = this + other
		return this

	def _minus_eq(this, other):
		this = this - other
		return this

	def _times_eq(this, other):
		this = this * other
		return this

	def _divide_eq(this, other):
		this = this / other
		return this

	def _mod(this, other):
		return this % other
	
	def _mod_eq(this, other):
		this = this % other
		return this
	
	def size(this):
		return len(this)

	def length(this):
		return this.size()
	

def CreateArithmeticFunction(functionName):
	return lambda this, *args: getattr(this.value if this.value is not None else this, functionName)(*args)
	
for name in [
	"__add__",
	"__sub__",
	"__mul__",
	"__matmul__",
	"__truediv__",
	"__floordiv__",
	"__mod__",
	"__divmod__",
	"__pow__",
	"__lshift__",
	"__rshift__",
	"__and__",
	"__xor__",
	"__or__",
	"__iadd__",
	"__isub__",
	"__imul__",
	"__imatmul__",
	"__itruediv__",
	"__ifloordiv__",
	"__imod__",
	"__ipow__",
	"__ilshift__",
	"__irshift__",
	"__iand__",
	"__ixor__",
	"__ior__",
	"__lt__",
	"__le__",
	"__eq__",
	"__ne__",
	"__gt__",
	"__ge__",
	"__bool__",
	"__str__",
	"__int__",
	"__float__",
	"__len__",
]:
	setattr(_type, name, CreateArithmeticFunction(name))
