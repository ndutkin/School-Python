>>> from homework26 import *
>>> dictionary_exceptions("Rose",{"Rose": 3.5,"Lily": 4.0,"Tulip": 2.5})
The price of Rose is $3.5
>>> dictionary_exceptions("Tulipia",{"Rose": 3.5,"Lily": 4.0,"Tulip": 2.5})
Error: Flower not found! Please enter Rose, Lily, or Tulip.
>>> dictionary_exceptions("",{"Rose": 3.5,"Lily": 4.0,"Tulip": 2.5})
Error: Flower not found! Please enter Rose, Lily, or Tulip.
>>> dictionary_exceptions("Lily",{"Rose": 3.5,"Lily": 4.0,"Tulip": 2.5})
The price of Lily is $4.0
>>> string_exceptions(4,"Hello World")
The character at index 4 is: o
>>> string_exceptions("abc","Hello World")
Error: String indices must be integers, not 'str'
>>> string_exceptions(12, "Hello World")
Error: Index out of range! Please enter a valid index.
>>> string_exceptions(0,"")
Error: Index out of range! Please enter a valid index.