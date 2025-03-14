# ruff: noqa: ANN401

import datetime as dt
from collections.abc import Callable, Iterable, Sequence
from typing import (
    Any,
    ClassVar,
    Final,
    Protocol,
    SupportsIndex,
    SupportsInt,
    TypeAlias,
    TypedDict,
    final,
    overload,
    type_check_only,
)
from typing import Literal as L

from _typeshed import Incomplete, StrOrBytesPath, SupportsLenAndGetItem
from typing_extensions import CapsuleType, TypeAliasType, TypeVar, Unpack

import numpy as np
from numpy import (
    _AnyShapeType,
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
    _IntLike_co,
    _NestedSequence,
    _ShapeLike,
    _SupportsArrayFunc,
    _SupportsDType,
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
_SCT_co = TypeVar("_SCT_co", bound=generic, covariant=True)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype[Any])
_ArrayT = TypeVar("_ArrayT", bound=ndarray[Any, Any])
_ArrayT_co = TypeVar("_ArrayT_co", bound=ndarray[Any, Any], covariant=True)
_ReturnT = TypeVar("_ReturnT")
_IdentityT = TypeVar("_IdentityT", default=None)
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])

_Array: TypeAlias = ndarray[_ShapeT, dtype[_SCT]]
_Array1D: TypeAlias = _Array[tuple[int], _SCT]

_ToInt: TypeAlias = int | np.integer | np.bool
_ToDT64: TypeAlias = np.datetime64[Any] | _ToInt
_ToTD64: TypeAlias = np.timedelta64[Any] | _ToInt
_ToFloat: TypeAlias = float | np.floating | np.integer | np.bool

# accepts strings like "1993-06-29"
_ToDate: TypeAlias = _ToDT64 | dt.date | str
# accepts the same strings as `builtins.int`
_ToDelta: TypeAlias = np.timedelta64[Any] | SupportsIndex | SupportsInt | dt.timedelta | str
# the `TypeAliasType`s helps reduce type-checker error spaghetti output
_ToDateArray = TypeAliasType(
    "_ToDateArray",
    _ArrayLike[np.datetime64[Any] | np.floating | np.integer | np.character]
    | _NestedSequence[_ToDT64 | dt.date]
    | _NestedSequence[str],
)
_ToDeltaArray = TypeAliasType(
    "_ToDeltaArray",
    _ArrayLike[np.timedelta64[Any] | np.integer] | _NestedSequence[_ToDelta],
)
_WeekMask: TypeAlias = str | Sequence[L[0, 1] | bool | np.bool]

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
    "raise",
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
class _SupportsLenArray(Protocol[_SCT_co]):
    def __len__(self, /) -> int: ...
    def __array__(self, /) -> NDArray[_SCT_co]: ...

@type_check_only
class _ConstructorKwargs(TypedDict, total=False):
    device: L["cpu"] | None
    like: _SupportsArrayFunc | None

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
    def __getitem__(self, key: _GetItemKeys, /) -> bool: ...
    def __setitem__(self, key: _SetItemKeys, value: bool, /) -> None: ...

_monotonicity: Final[Callable[..., Any]]
_place: Final[Callable[..., Any]]
_reconstruct: Final[Callable[..., Any]]
_vec_string: Final[Callable[..., Any]]
correlate2: Final[Callable[..., Any]]
dragon4_positional: Final[Callable[..., Any]]
dragon4_scientific: Final[Callable[..., Any]]
interp_complex: Final[Callable[..., Any]]
set_datetimeparse_function: Final[Callable[..., None]]

# NOTE: keep in sync with `zeros` and `_core.numeric.ones`
@overload  # 1d shape, default dtype
def empty(
    shape: SupportsIndex,
    dtype: type[float] | None = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array1D[float64]: ...
@overload  # 1d shape, given dtype
def empty(
    shape: SupportsIndex,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> np.ndarray[tuple[int], _DTypeT]: ...
@overload  # 1d shape, given scalar-type
def empty(
    shape: SupportsIndex,
    dtype: _DTypeLike[_SCT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array1D[_SCT]: ...
@overload  # 1d shape, unknown dtype
def empty(
    shape: SupportsIndex,
    dtype: DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array1D[Any]: ...
@overload  # known shape, default dtype
def empty(
    shape: _AnyShapeType,
    dtype: type[float] | None = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array[_AnyShapeType, float64]: ...
@overload  # known shape, known dtype
def empty(  # type: ignore[overload-overlap]
    shape: _AnyShapeType,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> np.ndarray[_AnyShapeType, _DTypeT]: ...
@overload  # known shape, known scalar-type
def empty(
    shape: _AnyShapeType,
    dtype: _DTypeLike[_SCT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array[_AnyShapeType, _SCT]: ...
@overload  # known shape, unknown dtype
def empty(
    shape: _AnyShapeType,
    dtype: DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array[_AnyShapeType, Any]: ...
@overload  # unknown shape, default dtype
def empty(
    shape: _ShapeLike,
    dtype: type[float] | None = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> NDArray[float64]: ...
@overload  # unknown shape, given dtype
def empty(
    shape: _ShapeLike,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
@overload  # unknown shape, given scalar-type
def empty(
    shape: _ShapeLike,
    dtype: _DTypeLike[_SCT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> NDArray[_SCT]: ...
@overload  # unknown shape, unknown dtype
def empty(
    shape: _ShapeLike,
    dtype: DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> NDArray[Any]: ...

# NOTE: keep in sync with `empty` and `_core.numeric.ones`
@overload  # 1d shape, default dtype
def zeros(
    shape: SupportsIndex,
    dtype: type[float] | None = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array1D[float64]: ...
@overload  # 1d shape, given dtype
def zeros(
    shape: SupportsIndex,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> np.ndarray[tuple[int], _DTypeT]: ...
@overload  # 1d shape, given scalar-type
def zeros(
    shape: SupportsIndex,
    dtype: _DTypeLike[_SCT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array1D[_SCT]: ...
@overload  # 1d shape, unknown dtype
def zeros(
    shape: SupportsIndex,
    dtype: DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array1D[Any]: ...
@overload  # known shape, default dtype
def zeros(
    shape: _AnyShapeType,
    dtype: type[float] | None = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array[_AnyShapeType, float64]: ...
@overload  # known shape, known dtype
def zeros(  # type: ignore[overload-overlap]
    shape: _AnyShapeType,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> np.ndarray[_AnyShapeType, _DTypeT]: ...
@overload  # known shape, known scalar-type
def zeros(
    shape: _AnyShapeType,
    dtype: _DTypeLike[_SCT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array[_AnyShapeType, _SCT]: ...
@overload  # known shape, unknown dtype
def zeros(
    shape: _AnyShapeType,
    dtype: DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> _Array[_AnyShapeType, Any]: ...
@overload  # unknown shape, default dtype
def zeros(
    shape: _ShapeLike,
    dtype: type[float] | None = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> NDArray[float64]: ...
@overload  # unknown shape, given dtype
def zeros(
    shape: _ShapeLike,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
@overload  # unknown shape, given scalar-type
def zeros(
    shape: _ShapeLike,
    dtype: _DTypeLike[_SCT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> NDArray[_SCT]: ...
@overload  # unknown shape, unknown dtype
def zeros(
    shape: _ShapeLike,
    dtype: DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_ConstructorKwargs],
) -> NDArray[Any]: ...

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
    dtype: _DTypeLike[_SCT],
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[_SCT]: ...
@overload
def empty_like(
    prototype: object,
    dtype: DTypeLike | None = None,
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
    object: object,
    dtype: DTypeLike | None = ...,
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
    indices: _SupportsLenArray[np.integer] | _NestedSequence[_ToInt],
    shape: _ShapeLike,
    order: _OrderCF = ...,
) -> tuple[NDArray[intp], ...]: ...
@overload
def unravel_index(
    indices: _ArrayLikeInt_co,
    shape: _ShapeLike,
    order: _OrderCF = ...,
) -> tuple[Any, ...]: ...

@overload
def ravel_multi_index(
    multi_index: Sequence[_IntLike_co],
    dims: Sequence[SupportsIndex],
    mode: _ModeKind | tuple[_ModeKind, ...] = ...,
    order: _OrderCF = ...,
) -> intp: ...
@overload
def ravel_multi_index(
    multi_index: Sequence[_SupportsLenArray[np.integer] | _NestedSequence[_ToInt]],
    dims: Sequence[SupportsIndex],
    mode: _ModeKind | tuple[_ModeKind, ...] = ...,
    order: _OrderCF = ...,
) -> NDArray[intp]: ...
@overload
def ravel_multi_index(
    multi_index: Sequence[_ArrayLikeInt_co],
    dims: Sequence[SupportsIndex],
    mode: _ModeKind | tuple[_ModeKind, ...] = ...,
    order: _OrderCF = ...,
) -> Any: ...

# NOTE: Allow any sequence of array-like objects
@overload
def concatenate(
    arrays: _ArrayLike[_SCT],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: None = ...,
    casting: _CastingKind | None = ...,
) -> NDArray[_SCT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: None = ...,
    casting: _CastingKind | None = ...,
) -> NDArray[Any]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: _DTypeLike[_SCT],
    casting: _CastingKind | None = ...,
) -> NDArray[_SCT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: DTypeLike,
    casting: _CastingKind | None = ...,
) -> NDArray[Any]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    *,
    out: _ArrayT,
    dtype: DTypeLike = ...,
    casting: _CastingKind | None = ...,
) -> _ArrayT: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None,
    out: _ArrayT,
    *,
    dtype: DTypeLike = ...,
    casting: _CastingKind | None = ...,
) -> _ArrayT: ...

def inner(a: ArrayLike, b: ArrayLike, /) -> Incomplete: ...
def lexsort(keys: ArrayLike, axis: SupportsIndex | None = ...) -> Incomplete: ...

def min_scalar_type(a: ArrayLike, /) -> dtype[Incomplete]: ...
def result_type(*arrays_and_dtypes: ArrayLike | DTypeLike) -> dtype[Incomplete]: ...
def promote_types(type1: DTypeLike, type2: DTypeLike, /) -> dtype[Incomplete]: ...

@overload
def where(condition: ArrayLike, /) -> tuple[NDArray[intp], ...]: ...
@overload
def where(condition: ArrayLike, x: ArrayLike, y: ArrayLike, /) -> NDArray[Incomplete]: ...

def can_cast(from_: ArrayLike | DTypeLike, to: DTypeLike, casting: _CastingKind | None = ...) -> bool: ...

#
@overload
def dot(a: ArrayLike, b: ArrayLike, out: None = ...) -> Incomplete: ...
@overload
def dot(a: ArrayLike, b: ArrayLike, out: _ArrayT) -> _ArrayT: ...

#
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
    dtype: _DTypeLike[_SCT],
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asarray(
    a: object,
    dtype: DTypeLike | None = ...,
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
    dtype: _DTypeLike[_SCT],
    order: _OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asanyarray(
    a: object,
    dtype: DTypeLike | None = ...,
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
    dtype: _DTypeLike[_SCT],
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def ascontiguousarray(
    a: object,
    dtype: DTypeLike | None = ...,
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
    dtype: _DTypeLike[_SCT],
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asfortranarray(
    a: object,
    dtype: DTypeLike | None = ...,
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
    dtype: DTypeLike | None = ...,
    count: SupportsIndex = ...,
    *,
    sep: str,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

@overload
def frompyfunc(
    func: Callable[[Any], _ReturnT],
    /,
    nin: L[1],
    nout: L[1],
    *,
    identity: _IdentityT | None = None,
) -> _PyFunc_Nin1_Nout1[_ReturnT, _IdentityT]: ...
@overload
def frompyfunc(
    func: Callable[[Any, Any], _ReturnT],
    /,
    nin: L[2],
    nout: L[1],
    *,
    identity: _IdentityT | None = None,
) -> _PyFunc_Nin2_Nout1[_ReturnT, _IdentityT]: ...
@overload
def frompyfunc(
    func: Callable[..., _ReturnT],
    /,
    nin: L[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    nout: L[1],
    *,
    identity: _IdentityT | None = None,
) -> _PyFunc_Nin3P_Nout1[_ReturnT, _IdentityT, int]: ...
@overload
def frompyfunc(
    func: Callable[..., _2PTuple[_ReturnT]],
    /,
    nin: L[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    nout: L[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    *,
    identity: _IdentityT | None = None,
) -> _PyFunc_Nin1P_Nout2P[_ReturnT, _IdentityT, int, int]: ...
@overload
def frompyfunc(
    func: Callable[..., Any],
    /,
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
    dtype: DTypeLike | None = ...,
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
    dtype: DTypeLike | None = ...,
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
    dtype: DTypeLike | None = ...,
    count: SupportsIndex = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

#
@overload  # (stop, dtype=_)
def arange(
    stop: object,
    *,
    dtype: _DTypeLike[_SCT],
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[_SCT]: ...
@overload  # (start, stop step, dtype)
def arange(
    start: object,
    stop: object,
    step: object,
    dtype: _DTypeLike[_SCT],
    *,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[_SCT]: ...
@overload  # (start, stop, step?, dtype=)
def arange(
    start: object,
    stop: object,
    step: object = ...,
    *,
    dtype: _DTypeLike[_SCT],
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[_SCT]: ...
@overload  # (stop: int)
def arange(
    stop: int | np.int_,
    *,
    dtype: _DTypeLike[np.int_] | type[int] | None = None,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.int_]: ...
@overload  # (start: int, stop: int, step?: int)
def arange(
    start: int | np.int_,
    stop: int | np.int_,
    step: int | np.int_ = ...,
    dtype: _DTypeLike[np.int_] | type[int] | None = None,
    *,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.int_]: ...
@overload  # (stop: float)
def arange(
    stop: float | np.float64,
    *,
    dtype: _DTypeLike[np.float64] | type[float] | None = None,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.float64]: ...
@overload  # (start: float, stop: float, step?: float)
def arange(
    start: float | np.float64,
    stop: float | np.float64,
    step: float | np.float64 = ...,
    dtype: _DTypeLike[np.float64] | type[float] | None = None,
    *,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.float64]: ...
@overload  # int-like
def arange(
    stop: _ToInt,
    *,
    dtype: None = None,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.signedinteger]: ...
@overload  # int-like
def arange(
    start: _ToInt,
    stop: _ToInt,
    step: _ToInt = ...,
    dtype: None = None,
    *,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.signedinteger]: ...
@overload  # float-like
def arange(
    stop: _ToFloat,
    *,
    dtype: None = None,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.floating]: ...
@overload  # float-like
def arange(
    start: _ToFloat,
    stop: _ToFloat,
    step: _ToFloat = ...,
    dtype: None = None,
    *,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.floating]: ...
@overload  # timedelta64
def arange(
    stop: np.timedelta64,
    *,
    dtype: None = None,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.timedelta64]: ...
@overload  # timedelta64
def arange(
    start: _ToTD64,
    stop: np.timedelta64,
    step: _ToTD64 = ...,
    dtype: None = None,
    *,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.timedelta64]: ...
@overload  # timedelta64
def arange(
    start: np.timedelta64,
    stop: _ToTD64,
    step: _ToTD64 = ...,
    dtype: None = None,
    *,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.timedelta64]: ...
@overload  # datetime64  (requires both start and stop)
def arange(
    start: np.datetime64,
    stop: np.datetime64,
    step: _ToDT64 = ...,
    dtype: None = None,
    *,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[np.datetime64]: ...
@overload  # fallback
def arange(
    stop: object,
    *,
    dtype: DTypeLike,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[Any]: ...
@overload  # fallback
def arange(
    start: object,
    stop: object,
    step: object = ...,
    dtype: DTypeLike | None = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
    device: L["cpu"] | None = ...,
) -> _Array1D[Any]: ...

# The datetime functions perform unsafe casts to `datetime64[D]`,
# so a lot of different argument types are allowed here

def datetime_data(dtype: str | _DTypeLike[datetime64] | _DTypeLike[timedelta64], /) -> tuple[str, int]: ...

@overload
def busday_count(
    begindates: _ToDate,
    enddates: _ToDate,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> np.int_: ...
@overload
def busday_count(
    begindates: _ToDate | _ToDateArray,
    enddates: _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> NDArray[np.int_]: ...
@overload
def busday_count(
    begindates: _ToDateArray,
    enddates: _ToDate | _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> NDArray[np.int_]: ...
@overload
def busday_count(
    begindates: _ToDate | _ToDateArray,
    enddates: _ToDate | _ToDateArray,
    weekmask: _WeekMask,
    holidays: _ToDateArray | None,
    busdaycal: busdaycalendar | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def busday_count(
    begindates: _ToDate | _ToDateArray,
    enddates: _ToDate | _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def busday_offset(
    dates: _ToDate,
    offsets: _ToDelta,
    roll: _RollKind = "raise",
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> np.datetime64[dt.datetime]: ...
@overload
def busday_offset(
    dates: _ToDate | _ToDateArray,
    offsets: _ToDeltaArray,
    roll: _RollKind = "raise",
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> NDArray[np.datetime64[dt.datetime]]: ...
@overload
def busday_offset(
    dates: _ToDateArray,
    offsets: _ToDelta | _ToDeltaArray,
    roll: _RollKind = "raise",
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> NDArray[np.datetime64[dt.datetime]]: ...
@overload
def busday_offset(
    dates: _ToDate | _ToDateArray,
    offsets: _ToDelta | _ToDeltaArray,
    roll: _RollKind,
    weekmask: _WeekMask,
    holidays: _ToDateArray | None,
    busdaycal: busdaycalendar | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def busday_offset(
    dates: _ToDate | _ToDateArray,
    offsets: _ToDelta | _ToDeltaArray,
    roll: _RollKind = "raise",
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def is_busday(
    dates: _ToDate,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> np.bool: ...
@overload
def is_busday(
    dates: _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> NDArray[np.bool]: ...
@overload
def is_busday(
    dates: _ToDateArray,
    weekmask: _WeekMask,
    holidays: _ToDateArray | None,
    busdaycal: busdaycalendar | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def is_busday(
    dates: _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    *,
    out: _ArrayT,
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
