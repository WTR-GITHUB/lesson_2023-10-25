# You are given an input array of bigrams, and an array of words.
# Write a function that returns True if every single bigram from this array
# can be found at least once in an array of words.

# can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) ➞ True
# can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) ➞ False
#  "cu" does not exist in any of the words.
# can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ True
# can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]) ➞ False

from typing import List


def detect(looking_for: List[str], words_list: List[str]) -> bool:
    check_list: list = [x for x in looking_for if any(x in bi for bi in words_list)]
    if check_list == looking_for:
        return True
    return False
   
print(detect(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
print(detect(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
print(detect(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
print(detect(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))
