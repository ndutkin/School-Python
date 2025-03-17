>>> from homework23 import *
>>> group_by_first_letter(["apple", "banana", "apricot", "blueberry", "cherry"])
{'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
>>> group_by_first_letter(["date","dragonfruit","durian","grape", "grapefruit", "guava","mango", "melon", "mulberry"])
{'d': ['date', 'dragonfruit', 'durian'], 'g': ['grape', 'grapefruit', 'guava'], 'm': ['mango', 'melon', 'mulberry']}
>>> group_by_first_letter(["broccoli", "beetroot", "butternut","garlic", "ginger", "greenbean","papaya", "pineapple", "pumpkin"])
{'b': ['broccoli', 'beetroot', 'butternut'], 'g': ['garlic', 'ginger', 'greenbean'], 'p': ['papaya', 'pineapple', 'pumpkin']}
>>> convert_to_sentence(["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"])
'The quick brown fox jumps over the lazy dog.'
>>> convert_to_sentence(["Learning", "Python", "is", "fun", "and", "challenging", "but", "rewarding"])
'Learning Python is fun and challenging but rewarding.'