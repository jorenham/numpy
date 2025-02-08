# ruff: noqa: PYI015

import datetime as dt
from typing import Protocol, Self, assert_type, overload

from typing_extensions import TypeVar

import numpy as np

py_date: dt.date
py_dt: dt.datetime
py_td: dt.timedelta

np_dt: np.datetime64[dt.datetime]
np_dt_date: np.datetime64[dt.date]
np_dt_int: np.datetime64[int]
np_dt_nat: np.datetime64[None]

np_td: np.timedelta64[dt.timedelta]
np_td_int: np.timedelta64[int]
np_td_nat: np.timedelta64[None]

# ---------- static checks ----------

# py_date
assert_type(py_date - py_td, dt.date)
assert_type(py_date - py_date, dt.timedelta)
# py_dt
assert_type(py_dt - py_td, dt.datetime)
assert_type(py_dt - py_dt, dt.timedelta)
# np_dt
# assert_type(np_dt - py_date,    dt.timedelta)
assert_type(np_dt - py_dt,      dt.timedelta)
assert_type(np_dt - py_td,      dt.datetime)  # ❌ raises [operator]
assert_type(np_dt - np_dt,      np.timedelta64[dt.timedelta])
assert_type(np_dt - np_dt_date, np.timedelta64[dt.timedelta])
assert_type(np_dt - np_dt_int,  np.timedelta64[int])
assert_type(np_dt - np_dt_nat,  np.timedelta64[None])
assert_type(np_dt - np_td,      np.datetime64[dt.datetime])
assert_type(np_dt - np_td_int,  np.datetime64[int])
assert_type(np_dt - np_td_nat,  np.datetime64[None])
# np_date
assert_type(np_dt_date - py_date,    dt.timedelta)
# assert_type(np_dt_date - py_dt,      dt.timedelta)
assert_type(np_dt_date - py_td,      dt.date)  # ❌ raises [operator]
assert_type(np_dt_date - np_dt,      np.timedelta64[dt.timedelta])
assert_type(np_dt_date - np_dt_date, np.timedelta64[dt.timedelta])
assert_type(np_dt_date - np_dt_int,  np.timedelta64[int])
assert_type(np_dt_date - np_dt_nat,  np.timedelta64[None])
assert_type(np_dt_date - np_td,      np.datetime64[dt.date])
assert_type(np_dt_date - np_td_int,  np.datetime64[int])
assert_type(np_dt_date - np_td_nat,  np.datetime64[None])
# np_dt_int
# assert_type(np_dt_int - py_date,    dt.timedelta)
# assert_type(np_dt_int - py_dt,      dt.timedelta)
# assert_type(np_dt_int - py_td,      dt.date)  # ❌ raises [operator]
assert_type(np_dt_int - np_dt,      np.timedelta64[int])
assert_type(np_dt_int - np_dt_date, np.timedelta64[int])
assert_type(np_dt_int - np_dt_int,  np.timedelta64[int])
assert_type(np_dt_int - np_dt_nat,  np.timedelta64[None])
assert_type(np_dt_int - np_td,      np.datetime64[int])
assert_type(np_dt_int - np_td_int,  np.datetime64[int])
assert_type(np_dt_int - np_td_nat,  np.datetime64[None])
# np_nat
assert_type(np_dt_nat - np_dt,      np.timedelta64[None])
assert_type(np_dt_nat - np_dt_date, np.timedelta64[None])
assert_type(np_dt_nat - np_dt_int,  np.timedelta64[None])
assert_type(np_dt_nat - np_dt_nat,  np.timedelta64[None])
assert_type(np_dt_nat - np_td,      np.datetime64[None])
assert_type(np_dt_nat - np_td_int,  np.datetime64[None])
assert_type(np_dt_nat - np_td_nat,  np.datetime64[None])
# fmt: on


class Timedelta(Protocol):
    def __add__(self, other: Self, /) -> Self: ...
    def __radd__(self, other: Self, /) -> Self: ...
    def __sub__(self, other: Self, /) -> Self: ...
    def __rsub__(self, other: Self, /) -> Self: ...

_TimedeltaT = TypeVar("_TimedeltaT", bound=Timedelta, default=Timedelta)
_TimedeltaT_co = TypeVar("_TimedeltaT_co", bound=Timedelta, default=Timedelta, covariant=True)
_TimedeltaT_contra = TypeVar("_TimedeltaT_contra", bound=Timedelta, default=Timedelta, contravariant=True)

class Timestamp(Protocol[_TimedeltaT]):
    @overload
    def __sub__(self, other: Self, /) -> _TimedeltaT: ...
    @overload
    def __sub__(self, other: _TimedeltaT, /) -> Self: ...


class SupportsSubSelf(Protocol[_TimedeltaT_co]):
    def __sub__(self, other: Self, /) -> _TimedeltaT_co: ...


class SupportsSubTD(Protocol[_TimedeltaT_contra]):
    def __sub__(self, other: _TimedeltaT_contra, /) -> Self: ...


td: Timedelta = np_td

_a1: SupportsSubTD = py_dt  # ✅
_a2: SupportsSubTD = np_dt  # ✅
_a3: SupportsSubTD[np.timedelta64] = np_dt  # ❌

_b1: SupportsSubSelf = py_dt  # ✅
_b2: SupportsSubSelf = np_dt  # ✅
_b3: SupportsSubSelf[np.timedelta64] = np_dt  # ❌

# w/o generic
_5: Timestamp = py_dt  # ✅
_6: Timestamp = np_dt  # ❌ (not fixed by reorder)
# w/ generic
_7: Timestamp[dt.timedelta] = py_dt  # ✅
_8: Timestamp[np.timedelta64] = np_dt  # ❌ (not fixed by reorder)
# w/ nested generic
_9: Timestamp[np.timedelta64[dt.timedelta]] = np_dt  # ❌ (fixed by reorder)


def infer_td_type(x: Timestamp[_TimedeltaT]) -> Timestamp[_TimedeltaT]: ...

# mypy fails these but pyright passes
assert_type(infer_td_type(np_dt), Timestamp[np.timedelta64[dt.timedelta]])
assert_type(infer_td_type(np_dt_int), Timestamp[np.timedelta64[int]])
assert_type(infer_td_type(np_dt_nat), Timestamp[np.timedelta64[None]])
