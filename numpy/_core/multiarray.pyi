# ruff: noqa: ANN401

import datetime as dt
from collections.abc import Callable, Iterable, Sequence
from typing import (
    Any,
    ClassVar,
    Final,
    Protocol,
    SupportsIndex,
    TypeAlias,
    TypedDict,
    TypeVar,
    final,
    overload,
    type_check_only,
)
from typing import Literal as L

from _typeshed import StrOrBytesPath, SupportsLenAndGetItem
from typing_extensions import CapsuleType, Unpack

import numpy as np
from numpy import (
    _CastingKind,
    _ModeKind,
    _NDIterFlagsKind,
    _NDIterFlagsOp,
    _OrderCF,
    _OrderKACF,
    _SupportsBuffer,
    _SupportsFileMethods,
    broadcast,
    busdaycalendar,
    complexfloating,
    correlate,
    count_nonzero,
    datetime64,
    dtype,
    flatiter,
    float64,
    floating,
    from_dlpack,
    generic,
    int_,
    interp,
    intp,
    matmul,
    ndarray,
    nditer,
    signedinteger,
    str_,
    timedelta64,
    ufunc,
    uint8,
    unsignedinteger,
    vecdot,
)
from numpy import absolute as absolute
from numpy import add as add
from numpy import arccos as arccos
from numpy import arccosh as arccosh
from numpy import arcsin as arcsin
from numpy import arcsinh as arcsinh
from numpy import arctan as arctan
from numpy import arctan2 as arctan2
from numpy import arctanh as arctanh
from numpy import bitwise_and as bitwise_and
from numpy import bitwise_count as bitwise_count
from numpy import bitwise_or as bitwise_or
from numpy import bitwise_xor as bitwise_xor
from numpy import cbrt as cbrt
from numpy import ceil as ceil
from numpy import conjugate as conjugate
from numpy import copysign as copysign
from numpy import cos as cos
from numpy import cosh as cosh
from numpy import deg2rad as deg2rad
from numpy import degrees as degrees
from numpy import divide as divide
from numpy import divmod as divmod
from numpy import einsum as c_einsum
from numpy import equal as equal
from numpy import exp as exp
from numpy import exp2 as exp2
from numpy import expm1 as expm1
from numpy import fabs as fabs
from numpy import float_power as float_power
from numpy import floor as floor
from numpy import floor_divide as floor_divide
from numpy import fmax as fmax
from numpy import fmin as fmin
from numpy import fmod as fmod
from numpy import frexp as frexp
from numpy import gcd as gcd
from numpy import greater as greater
from numpy import greater_equal as greater_equal
from numpy import heaviside as heaviside
from numpy import hypot as hypot
from numpy import invert as invert
from numpy import isfinite as isfinite
from numpy import isinf as isinf
from numpy import isnan as isnan
from numpy import isnat as isnat
from numpy import lcm as lcm
from numpy import ldexp as ldexp
from numpy import left_shift as left_shift
from numpy import less as less
from numpy import less_equal as less_equal
from numpy import log as log
from numpy import log1p as log1p
from numpy import log2 as log2
from numpy import log10 as log10
from numpy import logaddexp as logaddexp
from numpy import logaddexp2 as logaddexp2
from numpy import logical_and as logical_and
from numpy import logical_not as logical_not
from numpy import logical_or as logical_or
from numpy import logical_xor as logical_xor
from numpy import matvec as matvec
from numpy import maximum as maximum
from numpy import minimum as minimum
from numpy import modf as modf
from numpy import multiply as multiply
from numpy import negative as negative
from numpy import nextafter as nextafter
from numpy import not_equal as not_equal
from numpy import positive as positive
from numpy import power as power
from numpy import rad2deg as rad2deg
from numpy import radians as radians
from numpy import reciprocal as reciprocal
from numpy import remainder as remainder
from numpy import right_shift as right_shift
from numpy import rint as rint
from numpy import sign as sign
from numpy import signbit as signbit
from numpy import sin as sin
from numpy import sinh as sinh
from numpy import spacing as spacing
from numpy import sqrt as sqrt
from numpy import square as square
from numpy import subtract as subtract
from numpy import tan as tan
from numpy import tanh as tanh
from numpy import trunc as trunc
from numpy import vecmat as vecmat
from numpy._globals import _CopyMode
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeBytes_co,
    _ArrayLikeComplex_co,
    _ArrayLikeDT64_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeObject_co,
    _ArrayLikeStr_co,
    _ArrayLikeTD64_co,
    _ArrayLikeUInt_co,
    _DTypeLike,
    _FloatLike_co,
    _IntLike_co,
    _NestedSequence,
    _ScalarLike_co,
    _ShapeLike,
    _SupportsArrayFunc,
    _SupportsDType,
    _TD64Like_co,
)
from numpy._typing._ufunc import (
    _2PTuple,
    _PyFunc_Nin1_Nout1,
    _PyFunc_Nin1P_Nout2P,
    _PyFunc_Nin2_Nout1,
    _PyFunc_Nin3P_Nout1,
)
from numpy.lib._array_utils_impl import normalize_axis_index

__all__ = [
    "ALLOW_THREADS",
    "BUFSIZE",
    "CLIP",
    "DATETIMEUNITS",
    "ITEM_HASOBJECT",
    "ITEM_IS_POINTER",
    "LIST_PICKLE",
    "MAXDIMS",
    "MAY_SHARE_BOUNDS",
    "MAY_SHARE_EXACT",
    "NEEDS_INIT",
    "NEEDS_PYAPI",
    "RAISE",
    "USE_GETITEM",
    "USE_SETITEM",
    "WRAP",
    "_ARRAY_API",
    "_flagdict",
    "_monotonicity",
    "_place",
    "_reconstruct",
    "_vec_string",
    "add_docstring",
    "arange",
    "array",
    "asanyarray",
    "asarray",
    "ascontiguousarray",
    "asfortranarray",
    "bincount",
    "broadcast",
    "busday_count",
    "busday_offset",
    "busdaycalendar",
    "c_einsum",
    "can_cast",
    "compare_chararrays",
    "concatenate",
    "copyto",
    "correlate",
    "correlate2",
    "count_nonzero",
    "datetime_as_string",
    "datetime_data",
    "dot",
    "dragon4_positional",
    "dragon4_scientific",
    "dtype",
    "empty",
    "empty_like",
    "error",
    "flagsobj",
    "flatiter",
    "format_longfloat",
    "from_dlpack",
    "frombuffer",
    "fromfile",
    "fromiter",
    "fromstring",
    "get_handler_name",
    "get_handler_version",
    "inner",
    "interp",
    "interp_complex",
    "is_busday",
    "lexsort",
    "matmul",
    "may_share_memory",
    "min_scalar_type",
    "ndarray",
    "nditer",
    "nested_iters",
    "normalize_axis_index",
    "packbits",
    "promote_types",
    "putmask",
    "ravel_multi_index",
    "result_type",
    "scalar",
    "set_datetimeparse_function",
    "set_typeDict",
    "shares_memory",
    "typeinfo",
    "unpackbits",
    "unravel_index",
    "vdot",
    "vecdot",
    "where",
    "zeros",
]

_SCT = TypeVar("_SCT", bound=generic)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype[Any])
_ArrayT = TypeVar("_ArrayT", bound=ndarray[Any, Any])
_ArrayT_co = TypeVar("_ArrayT_co", bound=ndarray[Any, Any], covariant=True)
_ReturnT = TypeVar("_ReturnT")
_IDType = TypeVar("_IDType")
_NInT = TypeVar("_NInT", bound=int)
_NOutT = TypeVar("_NOutT", bound=int)
_SizeT = TypeVar("_SizeT", bound=int)
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])

_Array: TypeAlias = ndarray[_ShapeT, dtype[_SCT]]
_Array1D: TypeAlias = _Array[tuple[int], _SCT]

# Valid time units
_UnitKind: TypeAlias = L[
    "Y",
    "M",
    "D",
    "h",
    "m",
    "s",
    "ms",
    "us", "μs",
    "ns",
    "ps",
    "fs",
    "as",
]  # fmt: skip
_RollKind: TypeAlias = L[
    # `raise` is deliberately excluded
    "nat",
    "forward",
    "following",
    "backward",
    "preceding",
    "modifiedfollowing",
    "modifiedpreceding",
]

_GetItemKeys: TypeAlias = L[
    "C", "CONTIGUOUS", "C_CONTIGUOUS",
    "F", "FORTRAN", "F_CONTIGUOUS",
    "W", "WRITEABLE",
    "B", "BEHAVED",
    "O", "OWNDATA",
    "A", "ALIGNED",
    "X", "WRITEBACKIFCOPY",
    "CA", "CARRAY",
    "FA", "FARRAY",
    "FNC", "FORC",
]  # fmt: skip
_SetItemKeys: TypeAlias = L[
    "A", "ALIGNED",
    "W", "WRITEABLE",
    "X", "WRITEBACKIFCOPY",
]  # fmt: skip

@type_check_only
class _SupportsArray(Protocol[_ArrayT_co]):
    def __array__(self, /) -> _ArrayT_co: ...

@type_check_only
class _KwargsEmpty(TypedDict, total=False):
    device: L["cpu"] | None
    like: _SupportsArrayFunc | None

@type_check_only
class _ConstructorEmpty(Protocol):
    # 1-D shape
    @overload
    def __call__(
        self, /,
        shape: _SizeT,
        dtype: None = ...,
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[tuple[_SizeT], float64]: ...
    @overload
    def __call__(
        self, /,
        shape: _SizeT,
        dtype: _DTypeT | _SupportsDType[_DTypeT],
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> ndarray[tuple[_SizeT], _DTypeT]: ...
    @overload
    def __call__(
        self, /,
        shape: _SizeT,
        dtype: type[_SCT],
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[tuple[_SizeT], _SCT]: ...
    @overload
    def __call__(
        self, /,
        shape: _SizeT,
        dtype: DTypeLike,
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[tuple[_SizeT], Any]: ...

    # known shape
    @overload
    def __call__(
        self, /,
        shape: _ShapeT,
        dtype: None = ...,
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[_ShapeT, float64]: ...
    @overload
    def __call__(
        self, /,
        shape: _ShapeT,
        dtype: _DTypeT | _SupportsDType[_DTypeT],
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> ndarray[_ShapeT, _DTypeT]: ...
    @overload
    def __call__(
        self, /,
        shape: _ShapeT,
        dtype: type[_SCT],
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[_ShapeT, _SCT]: ...
    @overload
    def __call__(
        self, /,
        shape: _ShapeT,
        dtype: DTypeLike,
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[_ShapeT, Any]: ...

    # unknown shape
    @overload
    def __call__(
        self, /,
        shape: _ShapeLike,
        dtype: None = ...,
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> NDArray[float64]: ...
    @overload
    def __call__(
        self, /,
        shape: _ShapeLike,
        dtype: _DTypeT | _SupportsDType[_DTypeT],
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> ndarray[Any, _DTypeT]: ...
    @overload
    def __call__(
        self, /,
        shape: _ShapeLike,
        dtype: type[_SCT],
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> NDArray[_SCT]: ...
    @overload
    def __call__(
        self, /,
        shape: _ShapeLike,
        dtype: DTypeLike,
        order: _OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> NDArray[Any]: ...

###

# from ._multiarray_umath
ITEM_HASOBJECT: Final = 1
LIST_PICKLE: Final = 2
ITEM_IS_POINTER: Final = 4
NEEDS_INIT: Final = 8
NEEDS_PYAPI: Final = 16
USE_GETITEM: Final = 32
USE_SETITEM: Final = 64
ALLOW_THREADS: Final[L[0, 1]] = ...
BUFSIZE: Final = 8192
CLIP: Final = 0
WRAP: Final = 1
RAISE: Final = 2
MAXDIMS: Final = 32
MAY_SHARE_BOUNDS: Final = 0
MAY_SHARE_EXACT: Final = -1
DATETIMEUNITS: Final[CapsuleType] = ...
_ARRAY_API: Final[CapsuleType] = ...

error: Final = Exception
tracemalloc_domain: Final = 389047
typeinfo: Final[dict[str, np.dtype[np.generic]]] = ...
_flagdict: Final[dict[str, int]] = ...


@final
class flagsobj:
    __hash__: ClassVar[None]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]
    aligned: bool
    # NOTE: deprecated
    # updateifcopy: bool
    writeable: bool
    writebackifcopy: bool
    @property
    def behaved(self) -> bool: ...
    @property
    def c_contiguous(self) -> bool: ...
    @property
    def carray(self) -> bool: ...
    @property
    def contiguous(self) -> bool: ...
    @property
    def f_contiguous(self) -> bool: ...
    @property
    def farray(self) -> bool: ...
    @property
    def fnc(self) -> bool: ...
    @property
    def forc(self) -> bool: ...
    @property
    def fortran(self) -> bool: ...
    @property
    def num(self) -> int: ...
    @property
    def owndata(self) -> bool: ...
    def __getitem__(self, key: _GetItemKeys) -> bool: ...
    def __setitem__(self, key: _SetItemKeys, value: bool) -> None: ...

_monotonicity: Final[Callable[..., Any]]
_place: Final[Callable[..., Any]]
_reconstruct: Final[Callable[..., Any]]
_vec_string: Final[Callable[..., Any]]
correlate2: Final[Callable[..., Any]]
dragon4_positional: Final[Callable[..., Any]]
dragon4_scientific: Final[Callable[..., Any]]
interp_complex: Final[Callable[..., Any]]
set_datetimeparse_function: Final[Callable[..., None]]

zeros: Final[_ConstructorEmpty]
empty: Final[_ConstructorEmpty]

#
def get_handler_name(a: NDArray[Any] = ..., /) -> str | None: ...
def get_handler_version(a: NDArray[Any] = ..., /) -> int | None: ...
def format_longfloat(x: np.longdouble, precision: int) -> str: ...
def scalar(dtype: _DTypeT, object: bytes | object = ...) -> ndarray[tuple[()], _DTypeT]: ...
def set_typeDict(dict_: dict[str, np.dtype[Any]], /) -> None: ...

#
@overload
def empty_like(
    prototype: _ArrayT,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> _ArrayT: ...
@overload
def empty_like(
    prototype: _ArrayLike[_SCT],
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[_SCT]: ...
@overload
def empty_like(
    prototype: object,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[Any]: ...
@overload
def empty_like(
    prototype: Any,
    dtype: _DTypeLike[_SCT],
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[_SCT]: ...
@overload
def empty_like(
    prototype: Any,
    dtype: DTypeLike,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[Any]: ...

@overload
def array(
    object: _ArrayT,
    dtype: None = ...,
    *,
    copy: bool | _CopyMode | None = ...,
    order: _OrderKACF = ...,
    subok: L[True],
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _ArrayT: ...
@overload
def array(
    object: _SupportsArray[_ArrayT],
    dtype: None = ...,
    *,
    copy: bool | _CopyMode | None = ...,
    order: _OrderKACF = ...,
    subok: L[True],
    ndmin: L[0] = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _ArrayT: ...
@overload
def array(
    object: _ArrayLike[_SCT],
    dtype: None = ...,
    *,
    copy: bool | _CopyMode | None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def array(
    object: object,
    dtype: None = ...,
    *,
    copy: bool | _CopyMode | None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def array(
    object: Any,
    dtype: _DTypeLike[_SCT],
    *,
    copy: bool | _CopyMode | None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def array(
    object: Any,
    dtype: DTypeLike,
    *,
    copy: bool | _CopyMode | None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

@overload
def unravel_index(
    indices: _IntLike_co,
    shape: _ShapeLike,
    order: _OrderCF = ...,
) -> tuple[intp, ...]: ...
@overload
def unravel_index(
    indices: _ArrayLikeInt_co,
    shape: _ShapeLike,
    order: _OrderCF = ...,
) -> tuple[NDArray[intp], ...]: ...

@overload
def ravel_multi_index(
    multi_index: Sequence[_IntLike_co],
    dims: Sequence[SupportsIndex],
    mode: _ModeKind | tuple[_ModeKind, ...] = ...,
    order: _OrderCF = ...,
) -> intp: ...
@overload
def ravel_multi_index(
    multi_index: Sequence[_ArrayLikeInt_co],
    dims: Sequence[SupportsIndex],
    mode: _ModeKind | tuple[_ModeKind, ...] = ...,
    order: _OrderCF = ...,
) -> NDArray[intp]: ...

# NOTE: Allow any sequence of array-like objects
@overload
def concatenate(
    arrays: _ArrayLike[_SCT],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: None = ...,
    casting: _CastingKind | None = ...
) -> NDArray[_SCT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: None = ...,
    casting: _CastingKind | None = ...
) -> NDArray[Any]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: _DTypeLike[_SCT],
    casting: _CastingKind | None = ...
) -> NDArray[_SCT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: DTypeLike,
    casting: _CastingKind | None = ...
) -> NDArray[Any]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: _ArrayT = ...,
    *,
    dtype: DTypeLike = ...,
    casting: _CastingKind | None = ...
) -> _ArrayT: ...

def inner(
    a: ArrayLike,
    b: ArrayLike,
    /,
) -> Any: ...

@overload
def where(
    condition: ArrayLike,
    /,
) -> tuple[NDArray[intp], ...]: ...
@overload
def where(
    condition: ArrayLike,
    x: ArrayLike,
    y: ArrayLike,
    /,
) -> NDArray[Any]: ...

def lexsort(
    keys: ArrayLike,
    axis: SupportsIndex | None = ...,
) -> Any: ...

def can_cast(
    from_: ArrayLike | DTypeLike,
    to: DTypeLike,
    casting: _CastingKind | None = ...,
) -> bool: ...

def min_scalar_type(a: ArrayLike, /) -> dtype[Any]: ...
def result_type(*arrays_and_dtypes: ArrayLike | DTypeLike) -> dtype[Any]: ...
def promote_types(type1: DTypeLike, type2: DTypeLike, /) -> dtype[Any]: ...

@overload
def dot(a: ArrayLike, b: ArrayLike, out: None = ...) -> Any: ...
@overload
def dot(a: ArrayLike, b: ArrayLike, out: _ArrayT) -> _ArrayT: ...

@overload
def vdot(a: _ArrayLikeBool_co, b: _ArrayLikeBool_co, /) -> np.bool: ...
@overload
def vdot(a: _ArrayLikeUInt_co, b: _ArrayLikeUInt_co, /) -> unsignedinteger: ...
@overload
def vdot(a: _ArrayLikeInt_co, b: _ArrayLikeInt_co, /) -> signedinteger: ...
@overload
def vdot(a: _ArrayLikeFloat_co, b: _ArrayLikeFloat_co, /) -> floating: ...
@overload
def vdot(a: _ArrayLikeComplex_co, b: _ArrayLikeComplex_co, /) -> complexfloating: ...
@overload
def vdot(a: _ArrayLikeTD64_co, b: _ArrayLikeTD64_co, /) -> timedelta64: ...
@overload
def vdot(a: _ArrayLikeObject_co, b: object, /) -> Any: ...
@overload
def vdot(a: object, b: _ArrayLikeObject_co, /) -> Any: ...

def bincount(
    x: ArrayLike,
    /,
    weights: ArrayLike | None = ...,
    minlength: SupportsIndex = ...,
) -> NDArray[intp]: ...

def copyto(
    dst: NDArray[Any],
    src: ArrayLike,
    casting: _CastingKind | None = ...,
    where: _ArrayLikeBool_co | None = ...,
) -> None: ...

def putmask(
    a: NDArray[Any],
    /,
    mask: _ArrayLikeBool_co,
    values: ArrayLike,
) -> None: ...

def packbits(
    a: _ArrayLikeInt_co,
    /,
    axis: SupportsIndex | None = ...,
    bitorder: L["big", "little"] = ...,
) -> NDArray[uint8]: ...

def unpackbits(
    a: _ArrayLike[uint8],
    /,
    axis: SupportsIndex | None = ...,
    count: SupportsIndex | None = ...,
    bitorder: L["big", "little"] = ...,
) -> NDArray[uint8]: ...

def shares_memory(
    a: object,
    b: object,
    /,
    max_work: int | None = ...,
) -> bool: ...

def may_share_memory(
    a: object,
    b: object,
    /,
    max_work: int | None = ...,
) -> bool: ...

@overload
def asarray(
    a: _ArrayLike[_SCT],
    dtype: None = ...,
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asarray(
    a: object,
    dtype: None = ...,
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def asarray(
    a: Any,
    dtype: _DTypeLike[_SCT],
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asarray(
    a: Any,
    dtype: DTypeLike,
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

@overload
def asanyarray(
    a: _ArrayT,  # Preserve subclass-information
    dtype: None = ...,
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _ArrayT: ...
@overload
def asanyarray(
    a: _ArrayLike[_SCT],
    dtype: None = ...,
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asanyarray(
    a: object,
    dtype: None = ...,
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def asanyarray(
    a: Any,
    dtype: _DTypeLike[_SCT],
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asanyarray(
    a: Any,
    dtype: DTypeLike,
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

@overload
def ascontiguousarray(
    a: _ArrayLike[_SCT],
    dtype: None = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def ascontiguousarray(
    a: object,
    dtype: None = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def ascontiguousarray(
    a: Any,
    dtype: _DTypeLike[_SCT],
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def ascontiguousarray(
    a: Any,
    dtype: DTypeLike,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

@overload
def asfortranarray(
    a: _ArrayLike[_SCT],
    dtype: None = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asfortranarray(
    a: object,
    dtype: None = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def asfortranarray(
    a: Any,
    dtype: _DTypeLike[_SCT],
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asfortranarray(
    a: Any,
    dtype: DTypeLike,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

# `sep` is a de facto mandatory argument, as its default value is deprecated
@overload
def fromstring(
    string: str | bytes,
    dtype: None = ...,
    count: SupportsIndex = ...,
    *,
    sep: str,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[float64]: ...
@overload
def fromstring(
    string: str | bytes,
    dtype: _DTypeLike[_SCT],
    count: SupportsIndex = ...,
    *,
    sep: str,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def fromstring(
    string: str | bytes,
    dtype: DTypeLike,
    count: SupportsIndex = ...,
    *,
    sep: str,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

@overload
def frompyfunc(
    func: Callable[[Any], _ReturnT], /,
    nin: L[1],
    nout: L[1],
    *,
    identity: None = ...,
) -> _PyFunc_Nin1_Nout1[_ReturnT, None]: ...
@overload
def frompyfunc(
    func: Callable[[Any], _ReturnT], /,
    nin: L[1],
    nout: L[1],
    *,
    identity: _IDType,
) -> _PyFunc_Nin1_Nout1[_ReturnT, _IDType]: ...
@overload
def frompyfunc(
    func: Callable[[Any, Any], _ReturnT], /,
    nin: L[2],
    nout: L[1],
    *,
    identity: None = ...,
) -> _PyFunc_Nin2_Nout1[_ReturnT, None]: ...
@overload
def frompyfunc(
    func: Callable[[Any, Any], _ReturnT], /,
    nin: L[2],
    nout: L[1],
    *,
    identity: _IDType,
) -> _PyFunc_Nin2_Nout1[_ReturnT, _IDType]: ...
@overload
def frompyfunc(
    func: Callable[..., _ReturnT], /,
    nin: _NInT,
    nout: L[1],
    *,
    identity: None = ...,
) -> _PyFunc_Nin3P_Nout1[_ReturnT, None, _NInT]: ...
@overload
def frompyfunc(
    func: Callable[..., _ReturnT], /,
    nin: _NInT,
    nout: L[1],
    *,
    identity: _IDType,
) -> _PyFunc_Nin3P_Nout1[_ReturnT, _IDType, _NInT]: ...
@overload
def frompyfunc(
    func: Callable[..., _2PTuple[_ReturnT]], /,
    nin: _NInT,
    nout: _NOutT,
    *,
    identity: None = ...,
) -> _PyFunc_Nin1P_Nout2P[_ReturnT, None, _NInT, _NOutT]: ...
@overload
def frompyfunc(
    func: Callable[..., _2PTuple[_ReturnT]], /,
    nin: _NInT,
    nout: _NOutT,
    *,
    identity: _IDType,
) -> _PyFunc_Nin1P_Nout2P[_ReturnT, _IDType, _NInT, _NOutT]: ...
@overload
def frompyfunc(
    func: Callable[..., Any], /,
    nin: SupportsIndex,
    nout: SupportsIndex,
    *,
    identity: object | None = ...,
) -> ufunc: ...

@overload
def fromfile(
    file: StrOrBytesPath | _SupportsFileMethods,
    dtype: None = ...,
    count: SupportsIndex = ...,
    sep: str = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[float64]: ...
@overload
def fromfile(
    file: StrOrBytesPath | _SupportsFileMethods,
    dtype: _DTypeLike[_SCT],
    count: SupportsIndex = ...,
    sep: str = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def fromfile(
    file: StrOrBytesPath | _SupportsFileMethods,
    dtype: DTypeLike,
    count: SupportsIndex = ...,
    sep: str = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

@overload
def fromiter(
    iter: Iterable[Any],
    dtype: _DTypeLike[_SCT],
    count: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def fromiter(
    iter: Iterable[Any],
    dtype: DTypeLike,
    count: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

@overload
def frombuffer(
    buffer: _SupportsBuffer,
    dtype: None = ...,
    count: SupportsIndex = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[float64]: ...
@overload
def frombuffer(
    buffer: _SupportsBuffer,
    dtype: _DTypeLike[_SCT],
    count: SupportsIndex = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def frombuffer(
    buffer: _SupportsBuffer,
    dtype: DTypeLike,
    count: SupportsIndex = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

@overload
def arange(
    stop: _IntLike_co,
    /, *,
    dtype: None = ...,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[signedinteger]: ...
@overload
def arange(
    start: _IntLike_co,
    stop: _IntLike_co,
    step: _IntLike_co = ...,
    dtype: None = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[signedinteger]: ...
@overload
def arange(
    stop: _FloatLike_co,
    /, *,
    dtype: None = ...,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[floating]: ...
@overload
def arange(
    start: _FloatLike_co,
    stop: _FloatLike_co,
    step: _FloatLike_co = ...,
    dtype: None = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[floating]: ...
@overload
def arange(
    stop: _TD64Like_co,
    /, *,
    dtype: None = ...,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[timedelta64]: ...
@overload
def arange(
    start: _TD64Like_co,
    stop: _TD64Like_co,
    step: _TD64Like_co = ...,
    dtype: None = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[timedelta64]: ...
@overload
def arange(  # both start and stop must always be specified for datetime64
    start: datetime64,
    stop: datetime64,
    step: datetime64 = ...,
    dtype: None = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[datetime64]: ...
@overload
def arange(
    stop: Any,
    /, *,
    dtype: _DTypeLike[_SCT],
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[_SCT]: ...
@overload
def arange(
    start: Any,
    stop: Any,
    step: Any = ...,
    dtype: _DTypeLike[_SCT] = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[_SCT]: ...
@overload
def arange(
    stop: Any, /,
    *,
    dtype: DTypeLike,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[Any]: ...
@overload
def arange(
    start: Any,
    stop: Any,
    step: Any = ...,
    dtype: DTypeLike = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[Any]: ...

def datetime_data(
    dtype: str | _DTypeLike[datetime64] | _DTypeLike[timedelta64], /,
) -> tuple[str, int]: ...

# The datetime functions perform unsafe casts to `datetime64[D]`,
# so a lot of different argument types are allowed here

@overload
def busday_count(
    begindates: _ScalarLike_co | dt.date,
    enddates: _ScalarLike_co | dt.date,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> int_: ...
@overload
def busday_count(
    begindates: ArrayLike | dt.date | _NestedSequence[dt.date],
    enddates: ArrayLike | dt.date | _NestedSequence[dt.date],
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> NDArray[int_]: ...
@overload
def busday_count(
    begindates: ArrayLike | dt.date | _NestedSequence[dt.date],
    enddates: ArrayLike | dt.date | _NestedSequence[dt.date],
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: _ArrayT = ...,
) -> _ArrayT: ...

# `roll="raise"` is (more or less?) equivalent to `casting="safe"`
@overload
def busday_offset(
    dates: datetime64 | dt.date,
    offsets: _TD64Like_co | dt.timedelta,
    roll: L["raise"] = ...,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> datetime64: ...
@overload
def busday_offset(
    dates: _ArrayLike[datetime64] | dt.date | _NestedSequence[dt.date],
    offsets: _ArrayLikeTD64_co | dt.timedelta | _NestedSequence[dt.timedelta],
    roll: L["raise"] = ...,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> NDArray[datetime64]: ...
@overload
def busday_offset(
    dates: _ArrayLike[datetime64] | dt.date | _NestedSequence[dt.date],
    offsets: _ArrayLikeTD64_co | dt.timedelta | _NestedSequence[dt.timedelta],
    roll: L["raise"] = ...,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: _ArrayT = ...,
) -> _ArrayT: ...
@overload
def busday_offset(
    dates: _ScalarLike_co | dt.date,
    offsets: _ScalarLike_co | dt.timedelta,
    roll: _RollKind,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> datetime64: ...
@overload
def busday_offset(
    dates: ArrayLike | dt.date | _NestedSequence[dt.date],
    offsets: ArrayLike | dt.timedelta | _NestedSequence[dt.timedelta],
    roll: _RollKind,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> NDArray[datetime64]: ...
@overload
def busday_offset(
    dates: ArrayLike | dt.date | _NestedSequence[dt.date],
    offsets: ArrayLike | dt.timedelta | _NestedSequence[dt.timedelta],
    roll: _RollKind,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: _ArrayT = ...,
) -> _ArrayT: ...

@overload
def is_busday(
    dates: _ScalarLike_co | dt.date,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> np.bool: ...
@overload
def is_busday(
    dates: ArrayLike | _NestedSequence[dt.date],
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> NDArray[np.bool]: ...
@overload
def is_busday(
    dates: ArrayLike | _NestedSequence[dt.date],
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: _ArrayT = ...,
) -> _ArrayT: ...

@overload
def datetime_as_string(
    arr: datetime64 | dt.date,
    unit: L["auto"] | _UnitKind | None = ...,
    timezone: L["naive", "UTC", "local"] | dt.tzinfo = ...,
    casting: _CastingKind = ...,
) -> str_: ...
@overload
def datetime_as_string(
    arr: _ArrayLikeDT64_co | _NestedSequence[dt.date],
    unit: L["auto"] | _UnitKind | None = ...,
    timezone: L["naive", "UTC", "local"] | dt.tzinfo = ...,
    casting: _CastingKind = ...,
) -> NDArray[str_]: ...

@overload
def compare_chararrays(
    a1: _ArrayLikeStr_co,
    a2: _ArrayLikeStr_co,
    cmp: L["<", "<=", "==", ">=", ">", "!="],
    rstrip: bool,
) -> NDArray[np.bool]: ...
@overload
def compare_chararrays(
    a1: _ArrayLikeBytes_co,
    a2: _ArrayLikeBytes_co,
    cmp: L["<", "<=", "==", ">=", ">", "!="],
    rstrip: bool,
) -> NDArray[np.bool]: ...

def add_docstring(obj: Callable[..., Any], docstring: str, /) -> None: ...

def nested_iters(
    op: ArrayLike | Sequence[ArrayLike],
    axes: Sequence[Sequence[SupportsIndex]],
    flags: Sequence[_NDIterFlagsKind] | None = ...,
    op_flags: Sequence[Sequence[_NDIterFlagsOp]] | None = ...,
    op_dtypes: DTypeLike | Sequence[DTypeLike] = ...,
    order: _OrderKACF = ...,
    casting: _CastingKind = ...,
    buffersize: SupportsIndex = ...,
) -> tuple[nditer, ...]: ...
