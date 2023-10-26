def check_list(interesting_list: list) -> bool:
    return all(i == interesting_list[0] for i in interesting_list)

def add_alements(first_list: list, second_list: list):
    if len(first_list) == len(second_list):
        return check_list(list(map(lambda x: x[0] + x[1], list(zip(first_list, second_list)))))
    else:
        return "Two lists are not the same lenght"
    
print(add_alements([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))

# ==========================================================================
# from typing import List

# def splitevenodd(number_list: List[int]) -> int: 
#    evenlist = list(filter(lambda x: x % 2 == 0, number_list))
#    oddlist = list(filter(lambda x: x % 2 != 0, number_list))
#    print("Even lists:", evenlist) 
#    print("Odd lists:", oddlist)
#    if sum(evenlist) > sum(oddlist):
#       return f"Even numbers wins the difference is: {sum(evenlist) - sum(oddlist)}"
#    else:
#       return f"Odd numbers wins the difference is: {sum(oddlist) - sum(evenlist)}"

# print(splitevenodd([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))

# ==========================================================================
# from typing import List


# def detect(text: List[str], looking_for: List[str]) -> bool:
#     bigrams: List[str] = looking_for
#     return all(simb in text for simb in bigrams)
   
# print(detect(["maybe", "beta", "abet", "course"], ["ay", "be", "ta", "cu"]))