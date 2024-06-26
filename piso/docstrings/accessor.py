from piso.graph import adjacency_matrix

union_examples = """
Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()


Examples with *interval_arrays* empty:

>>> arr = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (2, 5), (3, 6), (7, 8), (8, 9), (10, 12)],
... )

>>> arr.piso.union()
<IntervalArray>
[(0.0, 6.0], (7.0, 9.0], (10.0, 12.0]]
Length: 3, closed: right, dtype: interval[float64]

>>> arr.set_closed("left").piso.union()
<IntervalArray>
[[0, 4), [2, 5), [3, 6), [7, 8), [8, 9), [10, 12)]
Length: 6, closed: left, dtype: interval[int64]

>>> pd.IntervalIndex(arr).piso.union()
IntervalIndex([(0.0, 6.0], (7.0, 9.0], (10.0, 12.0]],
              closed='right',
              dtype='interval[float64]')

>>> arr.piso.union(return_type=pd.IntervalIndex)
IntervalIndex([(0.0, 6.0], (7.0, 9.0], (10.0, 12.0]],
              closed='right',
              dtype='interval[float64]')


Examples with *interval_arrays* non empty:

>>> arr1 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (5, 6), (7, 8), (10, 12)],
... )
>>> arr2 = pd.arrays.IntervalArray.from_tuples(
...     [(3, 5), (8, 9)],
... )
>>> arr3 = pd.arrays.IntervalArray.from_tuples(
...     [(6, 8), (9, 11)],
... )

>>> arr1.piso.union(arr2)
<IntervalArray>
[(0.0, 6.0], (7.0, 9.0], (10.0, 12.0]]
Length: 3, closed: right, dtype: interval[float64]

>>> arr2.piso.union(arr3, return_type=pd.IntervalIndex)
IntervalIndex([(3.0, 5.0], (6.0, 11.0]],
              closed='right',
              dtype='interval[float64]')

>>> arr1.piso.union(arr2, arr3)
<IntervalArray>
[(0.0, 12.0]]
Length: 1, closed: right, dtype: interval[float64]

>>> arr1.piso.union(arr2, arr3, squeeze=True)
Interval(0.0, 12.0, closed='right')
"""

intersection_examples = """
Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()


Examples with *interval_arrays* empty:

>>> arr = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (2, 5), (3, 6)],
... )

>>> arr.piso.intersection()
<IntervalArray>
[(3.0, 4.0]]
Length: 1, closed: right, dtype: interval[float64]

>>> pd.IntervalIndex(arr).piso.intersection()
IntervalIndex([(3.0, 4.0]],
              closed='right',
              dtype='interval[float64]')

>>> arr.piso.intersection(return_type=pd.IntervalIndex)
IntervalIndex([(3.0, 4.0]],
              closed='right',
              dtype='interval[float64]')

>>> arr.piso.intersection(min_overlaps=2)
<IntervalArray>
[(2.0, 5.0]]
Length: 1, closed: right, dtype: interval[float64]

>>> arr2 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (2, 5), (3, 6), (7, 8), (8, 9), (10, 12)],
... )

>>> arr.piso.intersection()
<IntervalArray>
[]
Length: 0, closed: right, dtype: interval[int64]

>>> arr.piso.intersection(min_overlaps=2)
<IntervalArray>
[(2.0, 5.0]]
Length: 1, closed: right, dtype: interval[float64]

Examples with *interval_arrays* not empty:

>>> arr1 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (5, 6), (7, 8), (10, 12)],
... )
>>> arr2 = pd.arrays.IntervalArray.from_tuples(
...     [(3, 5), (8, 9)],
... )
>>> arr3 = pd.arrays.IntervalArray.from_tuples(
...     [(6, 8), (9, 11)],
... )

>>> arr1.piso.intersection(arr2)
<IntervalArray>
[(3.0, 4.0]]
Length: 1, closed: right, dtype: interval[float64]

>>> arr1.piso.intersection(arr2, squeeze=True)
Interval(3.0, 4.0, closed='right')

>>> arr1.piso.intersection(arr2, arr3)
<IntervalArray>
[]
Length: 0, closed: right, dtype: interval[float64]

>>> arr1.piso.intersection(arr2, arr3, min_overlaps=2)
<IntervalArray>
[(3.0, 4.0], (10.0, 11.0]]
Length: 2, closed: right, dtype: interval[float64]
"""

difference_examples = """
Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()


>>> arr1 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (2, 5), (3, 6), (7, 8), (8, 9), (10, 12)],
... )
>>> arr2 = pd.arrays.IntervalArray.from_tuples(
...     [(4, 7), (8, 11)],
... )
>>> arr3 = pd.arrays.IntervalArray.from_tuples(
...     [(2, 5), (7, 13)],
... )

>>> arr1.piso.difference(arr2)
<IntervalArray>
[(0.0, 4.0], (7.0, 8.0], (11.0, 12.0]]
Length: 3, closed: right, dtype: interval[float64]

>>> arr1.set_closed("left").piso.difference(arr2.set_closed("left"))
<IntervalArray>
[[0.0, 4.0), [7.0, 8.0), [11.0, 12.0)]
Length: 3, closed: left, dtype: interval[float64]

>>> arr1.piso.difference(arr2, return_type=pd.IntervalIndex)
IntervalIndex([(0.0, 4.0], (7.0, 8.0], (11.0, 12.0]],
              closed='right',
              dtype='interval[float64]')

>>> arr1.piso.difference(arr2, arr3)
<IntervalArray>
[(0.0, 2.0]]
Length: 1, closed: right, dtype: interval[float64]

>>> arr1.piso.difference(arr2, arr3, squeeze=True)
Interval(0.0, 2.0, closed='right')
"""

symmetric_difference_examples = """
Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()


Examples with *interval_arrays* empty:

>>> arr = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (2, 5), (3, 6), (7, 8), (8, 9), (10, 12)],
... )

>>> arr.piso.symmetric_difference()
<IntervalArray>
[(0.0, 2.0], (5.0, 6.0], (7.0, 9.0], (10.0, 12.0]]
Length: 4, closed: right, dtype: interval[float64]

>>> pd.IntervalIndex(arr).piso.symmetric_difference()
IntervalIndex([(0.0, 2.0], (5.0, 6.0], (7.0, 9.0], (10.0, 12.0]],
              closed='right',
              dtype='interval[float64]')

>>> arr.piso.symmetric_difference(return_type=pd.IntervalIndex)
IntervalIndex([(0.0, 2.0], (5.0, 6.0], (7.0, 9.0], (10.0, 12.0]],
              closed='right',
              dtype='interval[float64]')

>>> arr.piso.symmetric_difference(min_overlaps=3)
<IntervalArray>
[(0.0, 3.0], (4.0, 6.0], (7.0, 9.0], (10.0, 12.0]]
Length: 4, closed: right, dtype: interval[float64]

>>> arr.piso.symmetric_difference(min_overlaps="all")
<IntervalArray>
[(0.0, 6.0], (7.0, 9.0], (10.0, 12.0]]
Length: 3, closed: right, dtype: interval[float64]

Examples with *interval_arrays* non-empty:

>>> arr1 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (5, 6), (7, 8), (10, 12)],
... )
>>> arr2 = pd.arrays.IntervalArray.from_tuples(
...     [(3, 5), (8, 9)],
... )
>>> arr3 = pd.arrays.IntervalArray.from_tuples(
...     [(6, 8), (9, 11)],
... )

>>> arr1.piso.symmetric_difference(arr2)
<IntervalArray>
[(0.0, 3.0], (4.0, 6.0], (7.0, 9.0], (10.0, 12.0]]
Length: 4, closed: right, dtype: interval[float64]

>>> arr1.piso.symmetric_difference(arr2, arr3)
<IntervalArray>
[(0.0, 3.0], (4.0, 7.0], (8.0, 10.0], (11.0, 12.0]]
Length: 4, closed: right, dtype: interval[float64]

>>> arr1.piso.symmetric_difference(arr2, arr3, min_overlaps="all")
<IntervalArray>
[(0.0, 12.0]]
Length: 1, closed: right, dtype: interval[float64]
"""


isdisjoint_examples = """
Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()

>>> arr1 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 3), (2, 4)],
... )
>>> arr2 = pd.arrays.IntervalArray.from_tuples(
...     [(4, 7), (8, 11)],
... )
>>> arr3 = pd.arrays.IntervalArray.from_tuples(
...     [(2, 4), (7, 8)],
... )

>>> arr1.piso.isdisjoint()
False

>>> arr2.piso.isdisjoint()
True

>>> arr1.piso.isdisjoint(arr2)
True

>>> arr1.piso.isdisjoint(arr3)
False
"""

issuperset_examples = """
Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()

>>> arr1 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (3, 6), (7, 8), (10, 12)],
... )
>>> arr2 = pd.arrays.IntervalArray.from_tuples(
...     [(2, 5), (7, 8)],
... )
>>> arr3 = pd.arrays.IntervalArray.from_tuples(
...     [(3, 4), (10, 11)],
... )

>>> arr1.piso.issuperset(arr2)
True

>>> arr1.piso.issuperset(arr2, squeeze=False)
array([ True])

>>> arr1.piso.issuperset(arr2, arr3)
array([ True, True])

>>> arr2.piso.issuperset(arr3)
False
"""


issubset_examples = """
Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()

>>> arr1 = pd.arrays.IntervalArray.from_tuples(
...     [(2, 5), (7, 8)],
... )
>>> arr2 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (3, 6), (7, 8), (10, 12)],
... )
>>> arr3 = pd.arrays.IntervalArray.from_tuples(
...     [(3, 4), (10, 11)],
... )

>>> arr1.piso.issubset(arr2)
True

>>> arr1.piso.issubset(arr2, squeeze=False)
array([ True])

>>> arr1.piso.issubset(arr2, arr3)
array([ True, False])

>>> arr1.piso.issubset(arr3)
False
"""


def join_params(list_of_param_strings):
    return "".join(list_of_param_strings).replace("\n\n", "\n")


param_optional_args = """
*interval_arrays : argument list of :class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`
    May contain zero or more arguments.
"""

param_optional_args_min_one = """
*interval_arrays : argument list of :class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`
    Must contain at least one argument.
"""

param_min_overlaps = """
min_overlaps : int or "all", default "all"
    Specifies the minimum number of intervals which overlap in order to define an *intersection*.
    If *min_overlaps* is an int then it must be no smaller than 2.  If *min_overlaps* is all then
    an intersection is only defined where every interval overlaps.
    If supplied, must be done so as a keyword argument.
"""

param_squeeze = """
squeeze : boolean, default {default}
    If True, will try to coerce the return value to a single pandas.Interval.
    If supplied, must be done so as a keyword argument.
"""

param_return_type = """
return_type : {"infer", :class:`pandas.IntervalIndex`, :class:`pandas.arrays.IntervalArray`}, default "infer"
    If "infer" the return type will be the same as *interval_array*.
    If supplied, must be done so as a keyword argument.
"""

template_doc = """
What is considered a set is determined by the number of positional arguments used, that is, determined by the
size of *interval_arrays*.

If *interval_arrays* is empty then the sets are considered to be the intervals contained in the array object the
accessor belongs to (an instance of :class:`pandas.IntervalIndex`, :class:`pandas.arrays.IntervalArray`).

If *interval_arrays* is not empty then the sets are considered to be the elements in *interval_arrays*, in addition to the
intervals in the array object the accessor belongs to.
Each of these arrays is assumed to contain disjoint intervals (and satisfy the definition of a set).  Any array containing
overlaps between intervals will be mapped to one with disjoint intervals via a union operation.

{extra_desc}
Parameters
----------
{params}

Returns
-------
{return_type}

{examples}
"""

operation_template_doc = (
    """
Performs a set {operation} operation.
"""
    + template_doc
)

doc_difference_template = """
Performs a set difference operation.

The array elements of *interval_arrays*, and the interval array object the accessor belongs to
(an instance of :class:`pandas.IntervalIndex`, :class:`pandas.arrays.IntervalArray`) are considered to be the sets over which
the operation is performed.  Each of these arrays is assumed to contain disjoint intervals (and satisfy the definition of a set).
Any array containing overlaps between intervals will be mapped to one with disjoint intervals via a union operation.

The list *interval_arrays* must contain at least one element.  If *interval_arrays* contains a single element then
the result is the set difference between the interval array the accessor belongs to, and this single element.
If *interval_arrays* contains multiple elements then the result is the set difference between the interval array the accessor belongs to
and the union of the sets in *interval_arrays*.  This is equivalent to iteratively applying a set difference operation with each array
in *interval_arrays* as the second operand.

{extra_desc}
Parameters
----------
{params}

Returns
-------
:class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`

{examples}
"""

is_super_sub_set_template = """
Indicates whether a set is a {operation} of one, or more, other sets.

The array elements of *interval_arrays*, and the interval array object the accessor belongs to
(an instance of :class:`pandas.IntervalIndex`, :class:`pandas.arrays.IntervalArray`) are considered to be the sets over which
the operation is performed.  Each of these arrays is assumed to contain disjoint intervals (and satisfy the definition of a set).
Any array containing overlaps between intervals will be mapped to one with disjoint intervals via a union operation.

The list *interval_arrays* must contain at least one element.  The {operation} comparison is iteratively applied between
the interval array the accessor belongs to, and each array in *interval_arrays*.  When *interval_arrays* contains multiple
interval arrays, the return type will be a numpy array.  If it contains one interval array then the result can be coerced to
a single boolean using the *squeeze* parameter.

Parameters
----------
{params}

Returns
-------
:class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`

{examples}
"""

array_return_type = (
    ":class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`"
)

union_params = join_params(
    [
        param_optional_args,
        param_squeeze.format(default="False"),
        param_return_type,
    ]
)
union_docstring = operation_template_doc.format(
    operation="union",
    extra_desc="",
    params=union_params,
    return_type=array_return_type,
    examples=union_examples,
)

intersection_params = join_params(
    [
        param_optional_args,
        param_min_overlaps,
        param_squeeze.format(default="False"),
        param_return_type,
    ]
)
intersection_docstring = operation_template_doc.format(
    operation="intersection",
    extra_desc="",
    params=intersection_params,
    return_type=array_return_type,
    examples=intersection_examples,
)

difference_params = join_params(
    [
        param_optional_args_min_one,
        param_squeeze.format(default="False"),
        param_return_type,
    ]
)
difference_docstring = doc_difference_template.format(
    operation="difference",
    extra_desc="",
    params=difference_params,
    return_type=array_return_type,
    examples=difference_examples,
)


symmetric_difference_params = join_params(
    [
        param_optional_args,
        param_min_overlaps,
        param_squeeze.format(default="False"),
        param_return_type,
    ]
)
symmetric_difference_extra_desc = """
The symmetric difference can be defined as the set difference, of the union and the intersection.
The parameter *min_overlaps* in :meth:`piso.intersection`, which defines the minimum number of intervals
in an overlap required to constitute an intersection, follows through to symmetric difference under this definition.
"""
symmetric_difference_docstring = operation_template_doc.format(
    operation="symmetric difference",
    extra_desc=symmetric_difference_extra_desc,
    params=symmetric_difference_params,
    return_type=array_return_type,
    examples=symmetric_difference_examples,
)


isdisjoint_doc = (
    """
Indicates whether one, or more, sets are disjoint or not.

*interval_array* must be left-closed or right-closed if \\*interval_arrays is non-empty.
If no arguments are provided then this restriction does not apply.
"""
    + template_doc
)

isdisjoint_params = join_params(
    [
        param_optional_args,
    ]
)
isdisjoint_docstring = isdisjoint_doc.format(
    extra_desc="",
    params=isdisjoint_params,
    return_type="boolean",
    examples=isdisjoint_examples,
)


issuperset_params = join_params(
    [
        param_optional_args_min_one,
        param_squeeze.format(default="True"),
    ]
)
issuperset_docstring = is_super_sub_set_template.format(
    operation="superset",
    params=issuperset_params,
    examples=issuperset_examples,
)

issubset_params = join_params(
    [
        param_optional_args_min_one,
        param_squeeze.format(default="True"),
    ]
)
issubset_docstring = is_super_sub_set_template.format(
    operation="subset",
    params=issubset_params,
    examples=issubset_examples,
)


coverage_docstring = """
Calculates the size of a domain (or possibly multiple domains) covered by a collection of intervals.

The intervals are contained in the array object the accessor belongs to.
The (possibly overlapping) intervals may not, or partially, or wholly cover the domain.

Calculation over multiple domains is only possible when *bins* = True.

Parameters
----------
domain : :py:class:`tuple`, :class:`pandas.Interval`, :class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`, optional
    Specifies the domain over which to calculate the "coverage".  If *domain* is `None`,
    then the domain is considered to be the extremities of the intervals contained in the interval array the accessor belongs to.
    If *domain* is a tuple then it should specify lower and upper bounds, and be equivalent to a
    :class:`pandas.Interval`.  If *domain* is a :class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`
    then the intervals it contains define a possibly disconnected domain.
    If *bins* = True then *domain* must be :class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray` with disjoint intervals.
bins : boolean, default False
    If False, then the *domain* is interpreted as a single domain and returns one value.
    If True, then *domain* is interpreted as disjoint bins over which coverage is calculated for each.
how : {"fraction", "sum"}, default "fraction"
    If *how* = "fraction" then the result is a fraction of the size of the domain.
    If *how* = "sum" then the result is the length of the domain covered.

    .. versionadded:: 0.8.0

Returns
-------
float or :class:`pandas.Series`

Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()

>>> arr1 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (3, 5), (7, 8)],
... )

>>> arr1.piso.coverage()
0.75

>>> arr1.piso.coverage((0, 10))
0.6

>>> arr1.piso.coverage(pd.Interval(-10, 10))
0.3

>>> arr1.piso.coverage(pd.Interval(-10, 10), how="sum")
6

>>> domain = pd.arrays.IntervalArray.from_tuples(
...     [(4,6), (7, 10)],
... )
>>> arr1.piso.coverage(domain)
0.4

>>> arr1.piso.coverage(domain, bins=True)
(4, 6]     0.500000
(7, 10]    0.333333
dtype: float64

>>> arr1.piso.coverage(domain, bins=True, how="sum")
(4, 6]     1.0
(7, 10]    1.0
dtype: float64
"""

complement_docstring = """
Calculates the complement of a collection of intervals (in an array) over some domain.

Equivalent to the set difference of the domain and the intervals in the array that the accessor
belongs to.

Parameters
----------
domain : :py:class:`tuple`, :class:`pandas.Interval`, :class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`, optional
    Specifies the domain over which to calculate the "complement".  If *domain* is `None`,
    then the domain is considered to be the extremities of the intervals contained in the interval array
    that the accessor belongs to. If *domain* is a tuple then it should specify lower and upper bounds, and be equivalent to a
    :class:`pandas.Interval`.  If *domain* is a :class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`
    then the intervals it contains define a possibly disconnected domain.

Returns
-------
:class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`
    The return type will be the same as the interval array object the accessor belongs to.

Examples
--------

>>> import pandas as pd
>>> import piso

>>> arr1 = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (3, 5), (7, 8)],
... )

>>> arr1.piso.complement()
<IntervalArray>
[(5, 7]]
Length: 1, closed: right, dtype: interval[int64]

>>> arr1.piso.complement((-5, 10))
<IntervalArray>
[(-5, 0], (5, 7], (8, 10]]
Length: 3, closed: right, dtype: interval[int64]

>>> arr1.piso.complement(pd.Interval(-5, 6))
<IntervalArray>
[(-5, 0], (5, 6]]
Length: 2, closed: right, dtype: interval[int64]

>>> domain = pd.arrays.IntervalArray.from_tuples(
...     [(-5,-2), (7,10)],
... )

>>> arr1.piso.complement(domain)
<IntervalArray>
[(-5, -2], (8, 10]]
Length: 2, closed: right, dtype: interval[int64]
"""

get_indexer_docstring = """
Given a set of disjoint intervals (contained in the interval array that the accessor belongs to)
and a value, or vector, *x*, returns the index positions of the interval which contains each value in x.

*interval_array* can be left-closed, right-closed, both or neither.

Parameters
----------
x : scalar, or array-like of scalars
    Values in *x* should belong to the same domain as the intervals contained in the interval array
    that the accessor belongs to.

Returns
-------
:class:`numpy.ndarray`
    Values will be integer.  If a point is not contained in any interval then the corresponding
    value is -1.

Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()

>>> arr = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (6, 8), (10, 12)],
... )

>>> arr.piso.get_indexer(11)
2

>>> arr.piso.get_indexer(8)
1

>>> arr.piso.get_indexer(9)
-1

>>> arr.piso.get_indexer([1,2,7,13])
array([ 0,  0,  1, -1], dtype=int64)
"""


contains_docstring = """
Evaluates the intersection of a set of intervals with a set of points.

The format of the result is dependent on the *result* parameter.  If *result = "cartesian"* then the
the function returns a 2-dimensional boolean mask *M* of shape *(m,n)* where *m* is the number of
intervals, and *n* is the number of points.  The element in the i-th row and j-th column is True if
the i-th interval contains the j-th point.

If *result = "points"* then the result is a 1-dimensional boolean mask of length *n*.
If *result = "intervals"* then the result is a 1-dimensional boolean mask of length *m*.

Parameters
----------
interval_array : :class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`
    Contains the intervals.  May be left-closed, right-closed, both, or neither.
x : scalar, or array-like of scalars
    Values in *x* should belong to the same domain as the intervals contained by the object the
    accessor belongs to.
include_index : boolean, default True
    Indicates whether to return a :class:`numpy.ndarray` or :class:`pandas.DataFrame` indexed
    by *interval_array* and column names equal to *x*
result : {"cartesian", "points", "intervals"}, default "cartesian"
    If *result* = "cartesian" then the result will be two dimensional, otherwise it will be
    one dimensional.
how : {"any", "all"}, default "any"
    Only relevant if *result* is not "cartesian".  This parameter indicates either:
    - a True value means any or all points are contained within an interval, or
    - a True value means any or all intervals contained a point.
    Which of these interpretations is dependent on the *result* parameter.

Returns
-------
:class:`numpy.ndarray`, :class:`pandas.DataFrame` or :class:`pandas.Series`
    One, or two, dimensional and boolean valued.  Return type dependent on *include_index* and *result*.

Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()

>>> arr = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (2, 5)],
... )

>>> arr.piso.contains(1)
            1
(0, 4]   True
(2, 5]  False

>>> arr.piso.contains([0, 1, 3, 4])
            0      1     3     4
(0, 4]  False   True  True  True
(2, 5]  False  False  True  True

>>> arr.piso.contains([0, 1, 3, 4], include_index=False)
array([[False,  True,  True,  True],
       [False, False,  True,  True]])

>>> arr.piso.contains([0, 1, 3, 4], result="points")
0    False
1     True
3     True
4     True
dtype: bool

>>> arr.piso.contains([0, 1, 3, 4], result="points", how="all")
0    False
1    False
3     True
4     True
dtype: bool

>>> arr.piso.contains([0, 1, 3, 4], result="intervals")
(0, 4]    True
(2, 5]    True
dtype: bool

>>> pd.IntervalIndex.from_tuples([(0,2)]).piso.contains(1, include_index=False)
array([[ True]])
"""


split_docstring = """
Given a set of intervals, and break points, splits the intervals into pieces wherever
the overlap a break point.

The intervals are contained in the object the accessor belongs to.  They may be left-closed,
right-closed, both, or neither, and contain overlapping intervals.

Parameters
----------
x : scalar, or array-like of scalars
    Values in *x* should belong to the same domain as the intervals in *interval_array*.
    May contain duplicates and be unsorted.

Returns
-------
:class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`
    Return type will be the same type as the object the accessor belongs to.

Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()

>>> arr = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (2, 5)],
... )

>>> arr.piso.split(3)
<IntervalArray>
[(0, 3], (3, 4], (2, 3], (3, 5]]
Length: 4, closed: right, dtype: interval[int64]

>>> arr.piso.split([3,3,3,3])
<IntervalArray>
[(0, 3], (3, 4], (2, 3], (3, 5]]
Length: 4, closed: right, dtype: interval[int64]

>>> arr = pd.IntervalIndex.from_tuples(
...     [(0, 4), (2, 5)], closed="neither",
... )

>>> arr.piso.split([1, 6, 4])
IntervalIndex([(0.0, 1.0), (1.0, 4.0), (2.0, 4.0), (4.0, 5.0)],
              closed='neither',
              dtype='interval[float64]')
"""


adjacency_matrix_docstring = """
Returns a 2D array (or dataframe) of boolean values indicating edges between nodes in a graph.

The set of nodes correspond to intervals and the edges are defined by the relationship
defined by the *edges* parameter.

Note that the diagonal is defined with False values by default.

Parameters
----------
edges : {"intersect", "disjoint"}, default "intersect"
    Defines the relationship that edges between nodes represent.
include_index : bool, default True
    If True then a :class:`pandas.DataFrame`, indexed by the intervals, is returned.
    If False then a :class:`numpy.ndarray` is returned.

Returns
-------
:class:`pandas.DataFrame` or :class:`numpy.ndarray`
    Boolean valued, symmetrical, with False along diagonal.

Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()

>>> arr = pd.arrays.IntervalArray.from_tuples(
...    [(0,4), (3,6), (5, 7), (8,9), (9,10)],
...    closed="both",
... )

>>> arr.piso.adjacency_matrix()
         [0, 4]  [3, 6]  [5, 7]  [8, 9]  [9, 10]
[0, 4]    False    True   False   False    False
[3, 6]     True   False    True   False    False
[5, 7]    False    True   False   False    False
[8, 9]    False   False   False   False     True
[9, 10]   False   False   False    True    False

>>> arr.piso.adjacency_matrix(arr, include_index=False)
array([[False,  True, False, False, False],
       [ True, False,  True, False, False],
       [False,  True, False, False, False],
       [False, False, False, False,  True],
       [False, False, False,  True, False]])

>>> arr.piso.adjacency_matrix(arr, edges="disjoint")
         [0, 4]  [3, 6]  [5, 7]  [8, 9]  [9, 10]
[0, 4]    False   False    True    True     True
[3, 6]    False   False   False    True     True
[5, 7]     True   False   False    True     True
[8, 9]     True    True    True   False    False
[9, 10]    True    True    True   False    False
"""


bridge_docstring = """
Given a set of intervals, and a threshold, merges intervals which are separated by a gap less than
or equal to the threshold.  Overlapping intervals will be merged, regardless of threshold value.

The intervals are contained in the object the accessor belongs to.  They may be left-closed,
or right-closed, and contain overlapping intervals.

Parameters
----------
threshold : scalar
    The value should belong to the domain that arises from a subtraction over the domain of the intervals.
    For instance, if intervals are timestamp data, then *threshold* should be timedelta.

Returns
-------
:class:`pandas.IntervalIndex` or :class:`pandas.arrays.IntervalArray`
    Return type will be the same type as the object the accessor belongs to.


Examples
--------

>>> import pandas as pd
>>> import piso
>>> piso.register_accessors()

>>> arr = pd.arrays.IntervalArray.from_tuples(
...     [(0, 4), (3, 5), (7, 8), (11, 12)],
... )

>>> arr.piso.bridge(threshold=1)
<IntervalArray>
[(0.0, 5.0], (7.0, 8.0], (11.0, 12.0]]
Length: 3, closed: right, dtype: interval[float64]

>>> arr.piso.bridge(threshold=2)
<IntervalArray>
[(0.0, 8.0], (11.0, 12.0]]
Length: 2, closed: right, dtype: interval[float64]

>>> arr.piso.bridge(threshold=3)
<IntervalArray>
[(0.0, 12.0]]
Length: 1, closed: right, dtype: interval[float64]
"""
