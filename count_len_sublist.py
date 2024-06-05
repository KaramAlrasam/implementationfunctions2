from collections import Counter
a=[1, 1, 2, 3, 4, 4.3, 5, 1]
b="automatically"
def m_counter(a)->list:
  """It is in charge to return sublist has key & value """
  #make empty list
  res=[]
  #make variable has zero value
  start=0
  v=0
  for i in range(len(a)):
    if a[start]!=a[i]:
      res.append([v,a[start]])
      start=i
      v=1
    else:
      v+=1
  res.append([v,a[start]])
  return res

#[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
#[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]


print(m_counter(a))
print(m_counter(b))
print("="*20)


from itertools import groupby

def m_counter2(m_list:list)->list:
  return [[len(list(g)),k]for k, g in groupby(m_list)]

print(m_counter2(a))
print(m_counter2(b))