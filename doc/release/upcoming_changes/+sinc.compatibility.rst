`numpy.sinc` is now a ufunc
---------------------------
`numpy.sinc` accepts the standard ufunc arguments, including ``out`` and
``where``. Its input is now positional-only. Change ``np.sinc(x=values)``
to ``np.sinc(values)``. Array types that override `numpy.sinc` should
implement ``__array_ufunc__``. The function previously dispatched through
``__array_function__``. The ufunc also preserves array subclasses by default,
including masks on `numpy.ma.MaskedArray` inputs.

For real numeric inputs, the result is now exactly zero at nonzero integers
and more accurate near those integers.
