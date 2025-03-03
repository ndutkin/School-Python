>>> from homework18 import *
>>> iterate_dictionary([1,2,3])
one
two
three
>>> iterate_dictionary([1,3,4])
one
three
Number not in dictionary
>>> iterate_dictionary([2,4,6])
two
Number not in dictionary
Number not in dictionary
>>> check_if_positive([-1,2,3])
not positive
2
3
>>> check_if_positive([3,5,-1,-9,4,13,-2])
3
5
not positive
not positive
4
13
not positive
>>> check_if_positive([4,4,3,-19,-10,78,-22,-1])
4
4
3
not positive
not positive
78
not positive
not positive
>>> division([100,0,2,7])
1.0
can't divide by zero
50.0
14.29
>>> division([0,0,0])
can't divide by zero
can't divide by zero
can't divide by zero
>>> division([1,-7,0,2,0])
100.0
-14.29
can't divide by zero
50.0
can't divide by zero