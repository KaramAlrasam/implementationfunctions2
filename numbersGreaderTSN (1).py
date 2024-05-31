def numbersGreaderTSN(m_list:list, item:int)->list:
  """It is in charge to retuen numbers in the list
  are greaders than specified number"""
  #raise error if the item is not existent
  if item  not in m_list:
    raise ValueError(f"{item } is not existent.")
  #sort the list to make the operation is quickly
  m_sorted=sorted(m_list)
  #find index item
  index=m_sorted.index(item)
  #if the item is greader one return None
  if m_sorted[index]==m_sorted[-1]:
    return None
  #start searching about the item is grader than specified
  #number
  for i in range(index,len(m_sorted)):
    if m_sorted[i]>m_sorted[index]:
      #and the return the extenssion
      return m_sorted[i:]
a=[1,2,3,4,5,6,7,8,9,10]
print(numbersGreaderTSN(a,5))