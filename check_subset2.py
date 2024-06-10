a=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
b=[[1, 3], [13, 15, 17]]
from itertools import chain
# from difflib import SequenceMatcher
def check_subset1(a_list:list, b_list:list)->bool:
  """It is in charge to check if the subset exists in nested list a"""
  ch=chain(b_list)
  return all(item in a_list for item in ch) 


print(check_subset1(a,b))

print("="*30)

def check_subset2(a_list:list, b_list:list)->bool:
  """It is in charge to check if the subset exists in nested list a"""
  return all(map(b_list.__contains__, a_list))

print(check_subset2(b, a))