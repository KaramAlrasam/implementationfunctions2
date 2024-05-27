def commen_items(a_list:list, b_list:list)->list:
  """It is in charge to give you the commen items in two lists"""
  #first you need to save the commen items in one list
  res=[]
  #make for loop on one list and make condition to find out which items is commen
  for item in a_list:
    if item in b_list:
      res.append(item)
  res=list(set(res))
  return res

a=[1,3,5,7,9]
b=[1,2,3,4,5,6,7,0]
print(list(set(a) & set(b)))
print(commen_items(a,b))