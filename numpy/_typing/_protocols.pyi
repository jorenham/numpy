
from typing import Protocol, type_check_only
from typing_extensions import CapsuleType, TypeVar

__all__ = [
    "_SupportsReal",
    "_SupportsImag",
    "_SupportsBool",
    "_SupportsAwait",
    "_SupportsContains",
    "_SupportsGetItem",
    "_SupportsIter",
    "_SupportsAIter",
    "_SupportsInvert",
    "_SupportsNeg",
    "_SupportsPos",
    "_SupportsInvert",
    "_SupportsEQ",
    "_SupportsNE",
    "_SupportsLT",
    "_SupportsLE",
    "_SupportsGT",
    "_SupportsGE",
    "_SupportsAdd",
    "_SupportsSub",
    "_SupportsMul",
    "_SupportsMatMul",
    "_SupportsTrueDiv",
    "_SupportsFloorDiv",
    "_SupportsPow",
    "_SupportsMod",
    "_SupportsLShift",
    "_SupportsRShift",
    "_SupportsAnd",
    "_SupportsXOr",
    "_SupportsOr",
    "_SupportsRAdd",
    "_SupportsRSub",
    "_SupportsRMul",
    "_SupportsRMatMul",
    "_SupportsRTrueDiv",
    "_SupportsRFloorDiv",
    "_SupportsRPow",
    "_SupportsRMod",
    "_SupportsRLShift",
    "_SupportsRRShift",
    "_SupportsRAnd",
    "_SupportsRXOr",
    "_SupportsROr",
    "_SupportsDLPack",
]

_T_contra = TypeVar("_T_contra", contravariant=True)
_T_co = TypeVar("_T_co", covariant=True)
_BoolT_co = TypeVar("_BoolT_co", covariant=True, bound=bool, default=bool)

# numeric properties

@type_check_only
class _SupportsReal(Protocol[_T_co]):
    @property
    def real(self) -> _T_co: ...

@type_check_only
class _SupportsImag(Protocol[_T_co]):
    @property
    def imag(self) -> _T_co: ...

# container ops

@type_check_only
class _SupportsBool(Protocol[_BoolT_co]):
    def __bool__(self, /) -> _BoolT_co: ...

@type_check_only
class _SupportsContains(Protocol[_T_contra, _BoolT_co]):
    def __contains__(self, x: _T_contra, /) -> _BoolT_co: ...

@type_check_only
class _SupportsGetItem(Protocol[_T_contra, _T_co]):
    def __getitem__(self, k: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsIter(Protocol[_T_co]):
    def __iter__(self, /) -> _T_co: ...

# async ops

@type_check_only
class _SupportsAwait(Protocol[_T_co]):
    def __await__(self, /) -> _T_co: ...

@type_check_only
class _SupportsAIter(Protocol[_T_co]):
    def __aiter__(self, /) -> _T_co: ...

# unary arithmetic ops

@type_check_only
class _SupportsInvert(Protocol[_T_co]):
    def __invert__(self, /) -> _T_co: ...

@type_check_only
class _SupportsNeg(Protocol[_T_co]):
    def __neg__(self, /) -> _T_co: ...

@type_check_only
class _SupportsPos(Protocol[_T_co]):
    def __pos__(self, /) -> _T_co: ...

# rich comparison ops

@type_check_only
class _SupportsEQ(Protocol[_T_contra, _T_co]):
    def __eq__(self, rhs: _T_contra, /) -> _T_co: ...  # type: ignore[override] # pyright: ignore[reportIncompatibleMethodOverride]

@type_check_only
class _SupportsNE(Protocol[_T_contra, _T_co]):
    def __ne__(self, rhs: _T_contra, /) -> _T_co: ...  # type: ignore[override] # pyright: ignore[reportIncompatibleMethodOverride]

@type_check_only
class _SupportsLT(Protocol[_T_contra, _T_co]):
    def __lt__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsLE(Protocol[_T_contra, _T_co]):
    def __le__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsGT(Protocol[_T_contra, _T_co]):
    def __gt__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsGE(Protocol[_T_contra, _T_co]):
    def __ge__(self, rhs: _T_contra, /) -> _T_co: ...

# arithmetic binops

@type_check_only
class _SupportsAdd(Protocol[_T_contra, _T_co]):
    def __add__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsSub(Protocol[_T_contra, _T_co]):
    def __sub__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsMul(Protocol[_T_contra, _T_co]):
    def __mul__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsMatMul(Protocol[_T_contra, _T_co]):
    def __matmul__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsTrueDiv(Protocol[_T_contra, _T_co]):
    def __truediv__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsFloorDiv(Protocol[_T_contra, _T_co]):
    def __floordiv__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsMod(Protocol[_T_contra, _T_co]):
    def __mod__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsPow(Protocol[_T_contra, _T_co]):
    def __pow__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsLShift(Protocol[_T_contra, _T_co]):
    def __lshift__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRShift(Protocol[_T_contra, _T_co]):
    def __rshift__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsAnd(Protocol[_T_contra, _T_co]):
    def __and__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsXOr(Protocol[_T_contra, _T_co]):
    def __xor__(self, rhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsOr(Protocol[_T_contra, _T_co]):
    def __or__(self, rhs: _T_contra, /) -> _T_co: ...

# reflected binops

@type_check_only
class _SupportsRAdd(Protocol[_T_contra, _T_co]):
    def __radd__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRSub(Protocol[_T_contra, _T_co]):
    def __rsub__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRMul(Protocol[_T_contra, _T_co]):
    def __rmul__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRMatMul(Protocol[_T_contra, _T_co]):
    def __rmatmul__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRTrueDiv(Protocol[_T_contra, _T_co]):
    def __rtruediv__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRFloorDiv(Protocol[_T_contra, _T_co]):
    def __rfloordiv__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRMod(Protocol[_T_contra, _T_co]):
    def __rmod__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRPow(Protocol[_T_contra, _T_co]):
    def __rpow__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRLShift(Protocol[_T_contra, _T_co]):
    def __rlshift__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRRShift(Protocol[_T_contra, _T_co]):
    def __rrshift__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRAnd(Protocol[_T_contra, _T_co]):
    def __rand__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsRXOr(Protocol[_T_contra, _T_co]):
    def __rxor__(self, lhs: _T_contra, /) -> _T_co: ...

@type_check_only
class _SupportsROr(Protocol[_T_contra, _T_co]):
    def __ror__(self, lhs: _T_contra, /) -> _T_co: ...

# array api

@type_check_only
class _SupportsDLPack(Protocol[_T_contra]):
    def __dlpack__(self, /, *, stream: _T_contra | None = None) -> CapsuleType: ...
