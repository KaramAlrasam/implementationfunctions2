from itertools import groupby
a=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
def shallow_list(m_list:list)->list:
  """It is in charge to convert flatting list into shallow list"""
  #make empty list
  res=[]
  start=0
  #make for loop 
  for i in range(len(m_list)):
    if m_list[i]!=m_list[start]:
      res.append(m_list[start:i])
      start=i
  res.append(m_list[start:])
  return res

print(shallow_list(a))