# There's a great war between the even and odd numbers. Many numbers already
# lost their lives in this war and it's your task to end this. You have to
# determine which group sums larger: the evens or the odds. The larger group
# wins.
# Create a function that takes a list of integers, sums the even and odd
# numbers separately, then returns the difference between the sums of the even
# and odd numbers.

# war_of_numbers([2, 8, 7, 5]) ➞ 2
# war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168

from typing import List


def splitevenodd(number_list: List[int]) -> int: 
   evenlist = [] 
   oddlist = [] 
   for i in number_list: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   print("Even lists:", evenlist) 
   print("Odd lists:", oddlist)
   if sum(evenlist) > sum(oddlist):
      return f"Even numbers wins the difference is: {sum(evenlist) - sum(oddlist)}"
   else:
      return f"Odd numbers wins the difference is: {sum(oddlist) - sum(evenlist)}"

print(splitevenodd([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))