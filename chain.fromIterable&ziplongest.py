def switch(a_list:list)->list:
  """It is in charge to switch whole items in the list"""
  #make for loop on the list
  for i in range(0,len(a_list),2):
    #make condtion to finde out the nuber does't rech to the end of the list
    if i+1!=len(a_list):
      a_list[i],a_list[i+1]=a_list[i+1],a_list[i]

  return a_list
a=[0,1,2,3,4,5]
print(a)
print(switch(a))
print("="*30)

# Import the 'zip_longest,' 'chain,' and 'tee' functions from the 'itertools' module
from itertools import zip_longest, chain

# Define a function named 'replace2copy' that takes a list 'lst' as input and returns a new list with elements rearranged
def replace2copy(lst):
   res=list(chain.from_iterable(zip_longest(lst[1::2],lst[::2])))
   return res
# Define a list 'n' containing numeric elements
n = [0, 1, 2, 3, 4, 5]
# print(n[0::2])

# Call the 'replace2copy' function with 'n' as the argument and print the result
print(replace2copy(n)) 
