>>> from homework20 import *
>>> convert_to_ascii("a")
97
>>> convert_to_ascii("Hello World")
[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
>>> convert_to_ascii("C")
67
>>> filter_non_ascii("H"+chr(233)+"llo World")
Hllo World
>>> filter_non_ascii("Hello World")
Hello World
>>> filter_non_ascii("Y"+chr(233)+"s, This is for "+chr(255)+"ou")
Ys, This is for ou